# Imports
import discord
from discord.ext import commands
import config

# Init bot
bot = commands.Bot(command_prefix='!')

# Main bot event
@bot.event
async def on_ready():
    print('The bot is online!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(config.TOKEN)