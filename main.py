import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=':', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def rcoin(ctx):
    await ctx.send("Кидаю монетку")
    time.sleep(1)
    c = random.randint(1, 2)
    if c == 1:
        await ctx.send("Орёл")
    elif c == 2:
        await ctx.send("Решка")    
bot.run("Secret token")
