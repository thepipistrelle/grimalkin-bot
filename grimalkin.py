#imports and set-up stuff
import discord
import random
from discord.ext import commands, tasks
from itertools import cycle

#set some variables
grimalkin = commands.Bot(command_prefix="*", intents = discord.Intents.all())

token = open("token.txt", "r").read()

bot_status = cycle(["god simulator", "oracle", "astrology readings daily", "pickle eating simulator"])

#status loop for bot
@tasks.loop(minutes=5)
async def change_status():
    await grimalkin.change_presence(activity=discord.Game(next(bot_status)))

#commands
##single tarot reading
@grimalkin.command(aliases=["reading", "tarotreading"])
async def tarot(ctx, *, question):
    #open up our card file and our description file in read mode. then assign to new variables as split lines.
    with open("card.txt", "r") as file1, open("description.txt") as file2:
        description_lines = file2.read().splitlines()
        card_lines = file1.read().splitlines()
        #get the initial card
        response_card = random.choice(card_lines)
        card = str(response_card)
        print(card)
        #get the description
        for line in description_lines:
            if any(description in line for description in description_lines):
                print(line)
        reading=str(line)
    #send message with the full reading.      
    await ctx.send(reading)

    ##

#start-up loads
@grimalkin.event 
async def on_ready():
    print("grimalkin has found the spectral wavelength")
    change_status.start()

#final run --- do NOT put anything under here
grimalkin.run(token)
#####################################################################################



