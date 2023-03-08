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
@grimalkin.command()
async def tarot(ctx, author, question):
    #open up our card file and our description file in read mode. then assign to new variables as split lines.
    with open("card.txt", "r") as file1:
        card_options=file1.read().splitlines()
        response_card=random.choice(card_options)
        card=str(response_card)
        print(card)
    #compare card to description list
    with open("description.txt", "r") as file2:
        descriptions=file2.readlines()
        for line in descriptions:
            if line.startswith(card):
                card_description=str(line)
                reading=(card_description.split(':', 1)[-1])
                print(reading)

                ##now time to set up our embed

                embed = discord.Embed(colour=discord.Colour.green(), title="your tarot card", description="here is a keyword description of your card.")

                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

                embed.add_field(name="your card:", value=card, inline=False)
                embed.add_field(name="the card's keyword description:", value=reading, inline=False)
                embed.set_image(url="https://drive.google.com/file/d/11V1aGl6VZX1L5r0PXEoy0mi6p7srHgTH/view?usp=share_link")
                embed.set_footer(text="here are some reaction options")
    #send message with the full reading.      
                await ctx.send(embed=embed)

#start-up loads
@grimalkin.event 
async def on_ready():
    print("grimalkin has found the spectral wavelength")
    change_status.start()

#final run --- do NOT put anything under here
grimalkin.run(token)
#####################################################################################
#new random search
#with open("card.txt", "r") as file1, open("description.txt") as file2:
 #       description_lines = file2.read().splitlines()
  #      card_lines = file1.read().splitlines()
   #     #get the initial card
    #    response_card = random.choice(card_lines)
     #   card = str(response_card)
      #  print(card)





#            with open("card.txt", "r") as file1, open("description.txt") as file2:
 #       description_lines = file2.read().splitlines()
  #      card_lines = file1.read().splitlines()
   #     #get the initial card
    #    response_card = random.choice(card_lines)
     #   card = str(response_card)
      ##  print(card)
        ###get the description
        #for line in description_lines:
           # if any(card in line for card in description_lines):
         #       reading=str(card)
          #      print(reading)