import discord
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


@client.command()
async def connect(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command()
async def disconnect(ctx):
    await ctx.voice_client.disconnect()


@client.command(aliases=['m'])
async def mute(ctx):
    channel = ctx.author.voice.channel
    for member in channel.members:
        await member.edit(mute=True)


@client.command(aliases=['u'])
async def unmute(ctx):
    channel = ctx.author.voice.channel
    for member in channel.members:
        await member.edit(mute=False)


client.run(TOKEN)