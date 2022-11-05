import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

load_dotenv()
TOKEN = os.getenv("TOKEN") # do configure your TOKEN in a .env file
client = commands.Bot(command_prefix="#", intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is logged in")

@client.command()
async def hi(ctx):
    await ctx.reply("hello,how are you?")

client.run(TOKEN)
