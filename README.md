# Clipboard to Telegram Trading Bot Automation

This project automates the process of sending a contract address (CA) from the clipboard directly to a Telegram trading bot using a custom Telegram bot API. It eliminates the need for manually copying and pasting the address into the Telegram chat window and triggers the action with the press of the "1" key.

## Features

- Monitors the clipboard for contract addresses (CAs).
- Sends the clipboard contents to a Telegram bot chat with the press of the "1" key.
- Efficient integration with Telegram's Bot API for sending messages directly.
- No need for manual interaction with the Telegram client once configured.

## Prerequisites

Before running this project, make sure you have the following:

1. **Python 3.x** installed on your machine.
2. A **Telegram bot** created using [BotFather](https://core.telegram.org/bots#botfather).
3. The **Telegram chat ID** where the message should be sent.
4. Installed Python libraries: `python-telegram-bot`, `pyperclip`, and `keyboard`.

## Installation

### 1. Install Python Libraries

To get started, you need to install the required Python libraries. You can do this via `pip`:

```bash
pip install python-telegram-bot pyperclip keyboard
```

### 2. Get Your Telegram Bot Token

Create your Telegram bot using [BotFather](https://core.telegram.org/bots#botfather) and retrieve the **API token** for your bot.

### 3. Get Your Chat ID

You need the **chat ID** of the target bot or user. You can obtain it by using the `getUpdates` method of the Telegram Bot API or by interacting with the bot.

## Configuration

Once the necessary libraries are installed, configure the following in the script:

- **API Token**: Set the `API_TOKEN` variable to your bot's API token.
- **Chat ID**: Set the `CHAT_ID` variable to your target bot's chat ID or user chat ID.

```python
API_TOKEN = 'your_telegram_bot_token'  # Replace with your bot's API token
CHAT_ID = 'your_chat_id'  # Replace with your chat ID or target bot's chat ID
```

## Usage

### 1. Run the Script

Once configured, you can run the script. The script will monitor your clipboard and send the contents to the Telegram bot when you press the "1" key.

```bash
python clipboard_to_telegram.py
```

### 2. Trigger with "1" Key Press

- When you press the "1" key, the script will grab the current clipboard content (such as a contract address) and send it to the Telegram bot chat you configured.
  
### 3. Script Behavior

- The script waits for the "1" key press.
- Once "1" is pressed, the clipboard content (contract address) is sent to the Telegram bot.

## How It Works

1. **Clipboard Monitoring**: The script listens for the "1" key press.
2. **Clipboard Content**: When the "1" key is pressed, it grabs the current content of the clipboard.
3. **Send to Telegram**: The content is sent to the Telegram bot chat automatically using the Telegram Bot API.

## Contributions

If you have any improvements, feel free to fork the project and submit a pull request.

## License

This project is licensed under the MIT License.

---

Let me know if you need any further adjustments to the README!
