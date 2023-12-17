##imports
import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

### cargamos variables de entorno
load_dotenv()
##estructura de control
BOT_PREFIX = "!!"
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')

#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')

# client = MyClient(intents=intents)
# client.run(DISCORD_TOKEN)

## INTENTS
intents = discord.Intents.all()

# main
bot = commands.Bot(command_prefix=BOT_PREFIX,description="hola soy un bot",intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("sincronizado correctamente")
    print(f"el bot {bot.user} ya esta prendido")

@bot.hybrid_command(name="ping", description = "test")
async def ping(interaction: discord.Interaction):
    await interaction.reply(content="pong!") 

bot.run(DISCORD_TOKEN)