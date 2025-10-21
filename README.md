# Discord Bot - Rephrizzle

A simple Discord bot built with Python and discord.py

## Quick Start with GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/palyam/discord-bot-rephrizzle)

1. Click the badge above or go to your repository and click "Code" → "Codespaces" → "Create codespace on main"
2. Wait for the Codespace to build (dependencies install automatically)
3. Create a `.env` file with your Discord token:
   ```bash
   cp .env.example .env
   ```
4. Edit `.env` and add your Discord bot token
5. Run the bot:
   ```bash
   python3 bot.py
   ```

The bot will run in the Codespace and stay online as long as the Codespace is active!

## Local Setup

1. Install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

3. Add your Discord bot token to the `.env` file:
```
DISCORD_TOKEN=your_actual_token_here
```

4. Get your bot token:
   - Go to https://discord.com/developers/applications
   - Create a new application or select an existing one
   - Go to the "Bot" section
   - Copy the token and paste it in your `.env` file

## Running the Bot

**In Codespaces or Linux/Mac:**
```bash
python3 bot.py
```

**On Windows:**
```bash
python bot.py
```

## Available Commands

- `!hello` - Bot says hello to you
- `!ping` - Check bot latency
- `!echo <message>` - Bot repeats your message
- `!info` - Display bot information
- `!help` - Show all available commands

## Bot Permissions

When inviting the bot to your server, make sure it has these permissions:
- Read Messages/View Channels
- Send Messages
- Embed Links
- Read Message History

## Invite URL Template

```
https://discord.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=274877908992&scope=bot
```

Replace `YOUR_CLIENT_ID` with your bot's client ID from the Discord Developer Portal.
