import discord
from discord import app_commands
from discord.ui import Button, View
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables
load_dotenv()

# Configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
client_openai = AsyncOpenAI(api_key=OPENAI_API_KEY)

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

# Style definitions with prompts
STYLES = {
    "💼 corp mode": {
        "name": "Professional",
        "prompt": "Rewrite this text in a highly professional, formal business tone. Use sophisticated vocabulary, proper grammar, and maintain a respectful, corporate voice."
    },
    "💬 keepin it real": {
        "name": "Casual",
        "prompt": "Rewrite this text in a casual, friendly, conversational tone. Use everyday language like you're talking to a friend. Keep it relaxed and natural."
    },
    "🤝 business szn": {
        "name": "Business",
        "prompt": "Rewrite this text in a business professional tone suitable for emails, proposals, or client communication. Be clear, concise, and action-oriented."
    },
    "✨ main character": {
        "name": "Creative",
        "prompt": "Rewrite this text in a creative, poetic, and expressive style. Use vivid imagery, metaphors, and engaging language. Make it captivating and unique."
    },
    "🎯 just fix it": {
        "name": "Default",
        "prompt": "Rewrite this text to be clear, grammatically correct, and well-structured. Fix any errors while maintaining the original tone and meaning."
    }
}


class StyleButton(Button):
    def __init__(self, style_emoji_name, original_text):
        super().__init__(
            label=style_emoji_name,
            style=discord.ButtonStyle.primary,
            custom_id=f"style_{style_emoji_name}"
        )
        self.style_name = style_emoji_name
        self.original_text = original_text

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()

        # Create initial message
        style_info = STYLES[self.style_name]
        embed = discord.Embed(
            title=f"{self.style_name} activated",
            description="⚡ rephrizzle is cooking...",
            color=0x8B5CF6
        )
        message = await interaction.followup.send(embed=embed)

        # Stream the response
        try:
            full_response = ""
            stream = await client_openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": style_info["prompt"]},
                    {"role": "user", "content": self.original_text}
                ],
                stream=True,
                max_tokens=500,
                temperature=0.7
            )

            chunk_count = 0
            async for chunk in stream:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    chunk_count += 1

                    # Update every 10 chunks to avoid rate limits
                    if chunk_count % 10 == 0:
                        embed.description = full_response + "▌"
                        try:
                            await message.edit(embed=embed)
                        except:
                            pass  # Ignore rate limit errors during streaming

            # Final update
            embed.description = full_response
            embed.set_footer(text="⚡ done fr fr | use /rephrase to try another style")
            await message.edit(embed=embed)

        except Exception as e:
            error_embed = discord.Embed(
                title="❌ oops, something broke",
                description=f"Error: {str(e)}\n\nMake sure your OPENAI_API_KEY is set correctly in .env",
                color=0xFF0000
            )
            await message.edit(embed=error_embed)


class StyleView(View):
    def __init__(self, original_text):
        super().__init__(timeout=300)  # 5 minute timeout

        # Add all style buttons
        for style_name in STYLES.keys():
            self.add_item(StyleButton(style_name, original_text))


@bot.event
async def on_ready():
    await tree.sync()
    print(f'⚡ rephrizzle logged in as {bot.user}')
    print(f'🔥 Bot is online - no cap!')
    print(f'📡 Connected to {len(bot.guilds)} servers')

    # Set bot status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="your vibes | /rephrase"
        )
    )


@tree.command(name="rephrase", description="rephrase your text in different styles fr fr")
@app_commands.describe(text="the text you want to rephrase")
async def rephrase(interaction: discord.Interaction, text: str):
    """Main rephrase command with style buttons"""

    if len(text) < 5:
        await interaction.response.send_message(
            "❌ text too short bestie, give me more to work with",
            ephemeral=True
        )
        return

    if len(text) > 1000:
        await interaction.response.send_message(
            "❌ whoa that's too much text! keep it under 1000 characters",
            ephemeral=True
        )
        return

    # Create embed with buttons
    embed = discord.Embed(
        title="✨ pick your vibe",
        description=f"**Original text:**\n```{text[:200]}{'...' if len(text) > 200 else ''}```",
        color=0x8B5CF6
    )
    embed.set_footer(text="Click a button below to rephrase")

    view = StyleView(text)
    await interaction.response.send_message(embed=embed, view=view)


@tree.command(name="about", description="learn about rephrizzle")
async def about(interaction: discord.Interaction):
    """About command"""
    embed = discord.Embed(
        title="⚡ rephrizzle",
        description="no cap, just better words",
        color=0x8B5CF6
    )
    embed.add_field(
        name="What I do",
        value="I rephrase your text in 5 different styles using AI",
        inline=False
    )
    embed.add_field(
        name="Styles Available",
        value="💼 corp mode\n💬 keepin it real\n🤝 business szn\n✨ main character\n🎯 just fix it",
        inline=False
    )
    embed.add_field(
        name="How to use",
        value="Use `/rephrase` and paste your text, then click a style button",
        inline=False
    )
    embed.set_footer(text="Built with discord.py + OpenAI")

    await interaction.response.send_message(embed=embed)


if __name__ == '__main__':
    if not DISCORD_TOKEN:
        print("❌ Error: DISCORD_TOKEN not found in .env file!")
        print("Please add your Discord bot token to .env")
        exit(1)

    if not OPENAI_API_KEY:
        print("❌ Error: OPENAI_API_KEY not found in .env file!")
        print("Please add your OpenAI API key to .env")
        exit(1)

    bot.run(DISCORD_TOKEN)
