
# Ethereum Wallet Generator

A Python desktop application for generating Ethereum wallets, creating BIP39 12-word seed phrases, and generating QR codes for Ethereum addresses.

## Features

- Generate Ethereum Private Keys
- Generate Ethereum Public Keys
- Generate Ethereum Wallet Addresses
- Generate 12-word BIP39 Seed Phrases
- Generate QR Codes for Ethereum Addresses
- Copy Private Keys, Public Keys, and Addresses
- Save QR Codes as PNG Images
- Modern GUI with a Dark Theme
- Scrollable User Interface

## Technologies Used

- Python
- Tkinter
- ttkbootstrap
- eth-account
- Mnemonic
- QRCode
- Pillow
- Secrets

## Requirements

Make sure Python is installed on your system.

Install the required libraries:

```bash
pip install mnemonic ttkbootstrap eth-account qrcode pillow
```

## How to Run

1. Clone this repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd ethereum-wallet-generator
```

3. Run the application:

```bash
python wallet_app.py
```

## Project Structure

```text
ethereum-wallet-generator/
│
├── wallet_app.py
├── README.md
└── requirements.txt
```

## Security Notice

This project is developed for educational and demonstration purposes.

- Never share your Private Key or Seed Phrase.
- Never upload real wallet credentials to GitHub.
- Do not use this application to store significant funds without a professional security audit.

## Author

**Abolfazl Goodarzi**

Computer Engineering Student | Python Developer
