import discord
# from discord import app_commands
from discord.ext import commands

##estructura de control
BOT_PREFIX = "!!"
DISCORD_TOKEN = "DISCORD_BOT_SECRET_TOKEN"

## INTENTS
intents = discord.Intents.all()

# main
bot = commands.Bot(command_prefix=BOT_PREFIX,description="hola soy un bot",intents=intents)

@bot.event
async def on_ready():
    print(f"el bot {bot.user} ya esta prendido")
    await bot.tree.sync()
    print("sincronizado correctamente")

@bot.hybrid_command(name="insignea", description = "slash command")
async def insignea(interaction: discord.Interaction):
    await interaction.reply(content="reclamar la insignea de desarrollador en unos dias:\n https://discord.com/developers/active-developer")

bot.run(DISCORD_TOKEN)