# ⚡ rephrizzle - AI Text Rephrasing Bot

> no cap, just better words

A Gen Z 2026-style Discord bot that rephrases your text into 5 different writing styles using AI. Built with discord.py and OpenAI.

## ✨ Features

**5 Writing Styles:**
- 💼 **corp mode** - Professional, formal business tone
- 💬 **keepin it real** - Casual, friendly conversation
- 🤝 **business szn** - Business professional for emails
- ✨ **main character** - Creative, poetic expression
- 🎯 **just fix it** - Clean grammar and clarity

**Real-time Streaming:** Watch the AI rephrase your text word-by-word with live streaming responses.

**Button Interface:** Simple click-to-select style buttons - no complex commands needed.

## 🚀 Quick Start with GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/palyam/discord-bot-rephrizzle)

1. Click the badge above or go to your repository and click "Code" → "Codespaces" → "Create codespace on main"
2. Wait for the Codespace to build (dependencies install automatically)
3. Create a `.env` file:
   ```bash
   cp .env.example .env
   ```
4. Edit `.env` and add your tokens:
   ```bash
   DISCORD_TOKEN=your_discord_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```
5. Run the bot:
   ```bash
   python3 bot.py
   ```

The bot will run in the cloud and stay online as long as the Codespace is active!

## 🛠️ Local Setup

### Prerequisites
- Python 3.8 or higher
- Discord bot token ([Get one here](https://discord.com/developers/applications))
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/palyam/discord-bot-rephrizzle.git
   cd discord-bot-rephrizzle
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your tokens:
   ```
   DISCORD_TOKEN=your_discord_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run the bot:**
   ```bash
   python3 bot.py  # or python bot.py on Windows
   ```

## 📝 Getting Your Tokens

### Discord Bot Token
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name (e.g., "rephrizzle")
3. Go to the "Bot" section in the sidebar
4. Click "Add Bot"
5. Under "Token", click "Reset Token" and copy it
6. Paste it in your `.env` file as `DISCORD_TOKEN`

### OpenAI API Key
1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (you won't see it again!)
5. Paste it in your `.env` file as `OPENAI_API_KEY`

**Note:** OpenAI API usage costs money. Check [OpenAI pricing](https://openai.com/pricing) for current rates.

## 🤖 Bot Setup & Permissions

### Invite the Bot to Your Server

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application
3. Go to "OAuth2" → "URL Generator"
4. Select scopes:
   - `bot`
   - `applications.commands`
5. Select permissions:
   - Read Messages/View Channels
   - Send Messages
   - Embed Links
   - Use Slash Commands
6. Copy the generated URL and open it in your browser
7. Select your server and authorize

**Quick Invite URL Template:**
```
https://discord.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=274877908992&scope=bot%20applications.commands
```
Replace `YOUR_CLIENT_ID` with your bot's client ID.

## 💬 Usage

### Slash Commands

**`/rephrase [text]`**
- Main command to rephrase text
- Displays 5 style buttons
- Click any button to see your text rephrased in that style

**`/about`**
- Learn about the bot and available styles

### Example
```
/rephrase I need help with this project ASAP
```
Then click a style button:
- 💼 corp mode → "I require immediate assistance with this project."
- 💬 keepin it real → "Yo, can someone help me out with this project real quick?"
- 🤝 business szn → "I would appreciate your assistance with this project at your earliest convenience."
- ✨ main character → "A quest beckons, and I seek a fellow traveler to join me in this urgent endeavor."
- 🎯 just fix it → "I need help with this project as soon as possible."

## 🎨 Customization

### Adding New Styles

Edit the `STYLES` dictionary in `bot.py`:

```python
STYLES = {
    "🔥 your style": {
        "name": "Your Style Name",
        "prompt": "Your custom prompt for the AI..."
    },
    # ... existing styles
}
```

### Changing Colors

Edit the embed colors in `bot.py`:
```python
color=0x8B5CF6  # Purple - change to any hex color
```

## 🐛 Troubleshooting

**Bot doesn't respond to slash commands:**
- Wait a few minutes after starting the bot (Discord syncs commands globally)
- Try kicking and re-inviting the bot with proper permissions
- Make sure you enabled "Message Content Intent" in Discord Developer Portal → Bot settings

**"OPENAI_API_KEY not found" error:**
- Make sure `.env` file exists in the same directory as `bot.py`
- Check that the key is correctly formatted: `OPENAI_API_KEY=sk-...`
- Don't use quotes around the key

**Rate limit errors:**
- The bot updates every 10 chunks during streaming to avoid rate limits
- If you still get errors, increase the chunk update interval in `bot.py` (line 92)

**OpenAI API errors:**
- Check your OpenAI account has credits available
- Verify your API key is valid
- Make sure you're using `gpt-3.5-turbo` model (cheaper than GPT-4)

## 📦 Dependencies

- `discord.py==2.3.2` - Discord bot framework
- `openai==1.12.0` - OpenAI API client
- `python-dotenv==1.0.0` - Environment variable management
- `aiohttp==3.9.1` - Async HTTP client for streaming

## 🌟 Credits

Built by [@palyam](https://github.com/palyam)

Powered by:
- [discord.py](https://github.com/Rapptz/discord.py)
- [OpenAI API](https://openai.com/)

## 📄 License

MIT License - feel free to use and modify!

## 🔗 Links

- [GitHub Repository](https://github.com/palyam/discord-bot-rephrizzle)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [OpenAI Platform](https://platform.openai.com/)
