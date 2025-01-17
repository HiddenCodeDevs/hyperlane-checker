import cloudscraper
import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed



print("""



  _    _ _     _     _             _____          _
 | |  | (_)   | |   | |           / ____|        | |
 | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___
 |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \\
 | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
 |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|

            Orbiter Checker by Aero25x
            https://t.me/hidden_coding


    """)



# Define the URL template
URL_TEMPLATE = "https://api.orbiter.finance/sdk/opoints/user/{}"

# Define the headers
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en,en-US;q=0.9,ru;q=0.8",
    "Cache-Control": "max-age=0",
    "Priority": "u=0, i",
    "Sec-CH-UA": r'"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}

# Initialize a thread-safe total_tokens variable
total_tokens = 0.0
total_tokens_lock = threading.Lock()

def read_wallets(file_path: str) -> list:
    """
    Reads wallet addresses from a file, trims whitespace, and filters out invalid entries.
    """
    try:
        with open(file_path, 'r') as file:
            wallets = [
                line.strip()
                for line in file
                if line.strip() and len(line.strip()) == 42 and line.strip().startswith("0x")
            ]
        return wallets
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return []

def process_wallet(wallet: str, scraper: cloudscraper.CloudScraper) -> None:
    """
    Processes a single wallet: sends a GET request, parses the response, and updates total_tokens.
    """
    global total_tokens
    url = URL_TEMPLATE.format(wallet)

    try:
        response = scraper.get(url, headers=HEADERS, timeout=10)

        if response.status_code == 200:
            try:
                data = response.json()
                points = data.get("result", {}).get("points", None)

                if isinstance(points, (int, float)):
                    if points < 200.0:
                        print(f"{wallet} is not eligible (points: {points})")
                    else:
                        value = points * 5.5970149254
                        print("-" * 110)
                        print(f"[*]{wallet} is eligible (points: {points}, value: {value:.2f})")
                        print("-" * 110)
                        with total_tokens_lock:
                            total_tokens += value
                else:
                    print(f"{wallet}: Unable to fetch points from the response.")
            except json.JSONDecodeError:
                print(f"{wallet}: Failed to parse JSON response.")
            except Exception as e:
                print(f"{wallet}: An error occurred while processing the response: {e}")
        else:
            print(f"Failed to fetch data for wallet {wallet}. HTTP Status: {response.status_code}")

    except cloudscraper.exceptions.CloudflareChallengeError:
        print(f"{wallet}: Cloudflare challenge encountered.")
    except cloudscraper.exceptions.RequestException as e:
        print(f"{wallet}: Request failed: {e}")
    except Exception as e:
        print(f"{wallet}: An unexpected error occurred: {e}")

def main():
    wallets = read_wallets("wallets.txt")

    if not wallets:
        print("No valid wallets to process.")
        return

    scraper = cloudscraper.create_scraper()

    # Use ThreadPoolExecutor to handle concurrency
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(process_wallet, wallet, scraper): wallet for wallet in wallets}

        for future in as_completed(futures):
            wallet = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"An error occurred while processing wallet {wallet}: {e}")

    print("-" * 110)
    print(f"[*]Total Tokens: {total_tokens:.2f}")
    print("-" * 110)

    potential_usd_05 = total_tokens * 0.05
    potential_usd_03 = total_tokens * 0.03

    print(f"[*]Potential in USD if $0.05 per token: {potential_usd_05:.2f}$")
    print(f"[*]Potential in USD if $0.03 per token: {potential_usd_03:.2f}$")

if __name__ == "__main__":
    main()
