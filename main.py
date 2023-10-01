import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

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
async def pet(ctx): 
    await ctx.send("Моё любимое животное кошка.")   

    
bot.run("MTE1NTQ5OTk4MDc5NTE1MDQzNg.GJFCju.N89CRthEev_0N--dEgZDx7np05W2YiNG0XgBi8")
