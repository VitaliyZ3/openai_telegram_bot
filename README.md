# OpenAI Telegram Bot

A Telegram bot that integrates with OpenAI to provide various interactive features including random facts, GPT chat interface, and personality-based conversations.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create config file:**
   Create `config.py` with your API keys:
   ```python
   TG_BOT_API_KEY = "your_telegram_bot_token"
   OPENAI_API_KEY = "your_openai_api_key"
   ```

3. **Run the bot:**
   ```bash
   python src/bot.py
   ```

## Features

- `/start` - Welcome message with main menu
- Random fact generator with GPT integration
- Direct GPT chat interface  
- Personality-based conversations (Cobain, Hawking, Nietzsche, Queen, Tolkien)
- Quiz functionality

## Requirements

- Python 3.7+
- Telegram Bot Token (from @BotFather)
- OpenAI API Key