import os
import sys
import json
import disnake
from disnake.ext import commands

try:
    with open("config.json") as f:
        config = json.load(f)
except FileNotFoundError:
    print("config.json not found!")
    exit(1)

if not config["BOT_TOKEN"]:
    print("BOT_TOKEN not found!")
    exit(1)

if not config["BOT_PREFIX"]:
    print("BOT_PREFIX not found!")
    exit(1)

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=config["BOT_PREFIX"], intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Loaded {len(bot.commands)} commands")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(config["BOT_TOKEN"])