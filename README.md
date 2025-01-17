[![Join our Telegram RU](https://img.shields.io/badge/Telegram-RU-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aero25x)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aero25x)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@flaming_chameleon)
[![Reddit](https://img.shields.io/badge/Reddit-FF3A00?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/HiddenCode/)
[![Join our Telegram ENG](https://img.shields.io/badge/Telegram-EN-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding_en)



![image_2025-01-17_18-13-48](https://github.com/user-attachments/assets/956fc180-38a7-4eaa-8bfe-5aced8aa7400)

# Orbiter Checker by Aero25x


---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Input File Format](#input-file-format)
- [Output](#output)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---



**Orbiter Checker** is a Python-based tool designed to verify and process a list of cryptocurrency wallet addresses against the Orbiter Finance API. It checks each wallet's eligibility based on their points and calculates the potential token value based on predefined rates.

---

## Features

- **Wallet Validation**: Ensures each wallet address is valid (starts with `0x` and is 42 characters long).
- **API Integration**: Fetches wallet data from the Orbiter Finance API.
- **Eligibility Check**: Determines if a wallet is eligible based on points (≥ 200 points).
- **Token Calculation**: Calculates token value for eligible wallets.
- **USD Potential Calculation**: Computes potential USD value based on different token rates.
- **User-Friendly Output**: Provides clear and formatted console output for easy interpretation.

---

## Prerequisites

- **Python 3.6+**: Ensure you have Python installed on your system.
- **Pip**: Python package manager.

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Aero25x/orbiter-checker.git
   cd orbiter-checker
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies**

   ```bash
   pip install cloudscraper
   ```

   *Alternatively, if you have a `requirements.txt` file:*

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Prepare Wallets File**

   Create a `wallets.txt` file in the project directory and list each wallet address on a new line. Ensure each address:

   - Starts with `0x`
   - Is exactly 42 characters long

   **Example `wallets.txt`:**

   ```
   0xYourWalletAddress1
   0xYourWalletAddress2
   0xYourWalletAddress3
   ```

2. **Run the Script**

   ```bash
   python orbiter_checker.py
   ```

   **Sample Output:**

   ```
  
     _    _ _     _     _             _____          _
    | |  | (_)   | |   | |           / ____|        | |
    | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___
    |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \
    | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
    |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|

               Orbiter Checker by Aero25x
               https://t.me/hidden_coding


    0xYourWalletAddress1 is not eligible (points: 150)
    0xYourWalletAddress2 is eligible (points: 250, value: 1399.25)
    --------------------------------------------------
    [*]Total Tokens: 1399.25
    --------------------------------------------------
    [*]Potential in USD if $0.05 per token: 69.96$
    [*]Potential in USD if $0.03 per token: 41.98$
   ```

---

## Input File Format

- **File Name**: `wallets.txt`
- **Location**: Same directory as the script (or specify the path accordingly).
- **Format**: Plain text file with one wallet address per line.

**Example:**

```
0xAbC123...789
0xDef456...012
0xGhi789...345
```

---

## Output

After processing, the script provides:

- **Eligibility Status**: Indicates whether each wallet is eligible based on points.
- **Points and Token Value**: Displays the points and calculated token value for eligible wallets.
- **Total Tokens**: Sum of tokens from all eligible wallets.
- **Potential USD Values**: Calculates potential earnings based on two different token rates.


---

## Error Handling

The script is equipped to handle various errors gracefully:

- **File Not Found**: If `wallets.txt` is missing, an error message is displayed.
- **Invalid Wallet Addresses**: Wallets not starting with `0x` or not 42 characters long are skipped with a warning.
- **HTTP Errors**: Non-200 HTTP responses are reported.
- **JSON Parsing Errors**: If the API response cannot be parsed, an error is logged.
- **Cloudflare Challenges**: If Cloudflare challenges are encountered, a specific message is shown.
- **Unexpected Errors**: Any unforeseen errors are caught and reported.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add YourFeature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

   Describe your changes and submit for review.

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software as per the license terms.

---

## Contact

For support or inquiries, join our Telegram group:


---

## Acknowledgements

- **Cloudscraper**: For handling HTTP requests and bypassing Cloudflare protections.
- **Python Community**: For providing extensive resources and support.

---



```
  
  _    _ _     _     _             _____          _
 | |  | (_)   | |   | |           / ____|        | |
 | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___
 |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \
 | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
 |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|

            Orbiter Checker by Aero25x
            https://t.me/hidden_coding
```

[![Join our Telegram RU](https://img.shields.io/badge/Telegram-RU-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aero25x)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aero25x)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@flaming_chameleon)
[![Reddit](https://img.shields.io/badge/Reddit-FF3A00?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/HiddenCode/)
[![Join our Telegram ENG](https://img.shields.io/badge/Telegram-EN-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding_en)

