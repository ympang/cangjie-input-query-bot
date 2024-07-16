# Cangjie Input Query Bot

![Cangjie Input Query Bot](https://img.shields.io/badge/version-1.0-green) ![Python](https://img.shields.io/badge/python-3.8%2B-blue)

The **Cangjie Input Query Bot** is a Telegram bot that serves as a Cangjie dictionary. It allows users to input Chinese characters and receive their corresponding Cangjie codes, making it a useful tool for learners and users of the Cangjie input method.

## Features

- **Character to Cangjie Code:** Input Chinese characters and get the associated Cangjie code.
- **User-Friendly:** Simple interface for easy interaction through Telegram.

## Requirements

- Telegram Bot Token
- Docker

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ympang/cangjie-input-query-bot.git
   cd cangjie-input-query-bot

2. **Build the Docker image:**

   ```bash
   docker build -t cangjie-bot .
   
3. **Run the Docker container:**

   ```bash
   docker run -d --name cangjie-bot cangjie-bot

## Configuration

Ensure you set up your Telegram bot token in the **config.py**.

```bash
TOKEN = your_telegram_bot_token
