
bot.run("Secret token")
import os
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
    await ctx.send(f'{member.name} присоединился {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def rcoin(ctx):
    await ctx.send("Кидаю монетку")
    time.sleep(1)
    while True:
        c = random.randint(1, 2)
        if c == 1:
            await ctx.send("Орёл")
            break
        elif c == 2:
            await ctx.send("Решка") 
            break

@bot.command()
async def bhelp(ctx):
    await ctx.send("Можно использовать вот такие команды: ")
    await ctx.send(":hello")      
    await ctx.send(":heh Напишите цифру здесь")    
    await ctx.send(":rcoin")
    await ctx.send(":bhelp :)")  
    await ctx.send(":mball")       
    await ctx.send(":meme")

@bot.command() 
async def mball(ctx):
    await ctx.send("Добро пожаловать в магический шар")
    await ctx.send("Мыслено задайте вопрос")
    time.sleep(3)
    o = random.randint(1, 6)
    if o == 1:
        await ctx.send("Да")
    elif o == 2:
        await ctx.send("Нет")
    elif o == 3:
        await ctx.send("Если вы не сделаете этого то вам капут")
    elif o == 4:
        await ctx.send("Лучше полежите на диване")
    elif o == 5:
        await ctx.send("Ни в коем случаи не делайте этого")     
    elif o == 6:
        await ctx.send("Беги делать это.")    
     
@bot.command()
async def meme(ctx):
    MemeList = os.listdir("meme")
    rmeme = random.choice(MemeList)
    with open(f'meme/{rmeme}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)     
    
bot.run("Secret token")
