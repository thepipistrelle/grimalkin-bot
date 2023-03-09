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
    #open up the card.txt file, split into lines, and grab random card
    with open("card.txt", "r") as file1:
        card_options=file1.read().splitlines()
        response_card=random.choice(card_options)
        card=str(response_card)
        print(card)
    #compare card to find corresponding description for the card
    with open("description.txt", "r") as file2:
        descriptions=file2.readlines()
        for line in descriptions:
            if line.startswith(card):
                card_description=str(line)
                reading=(card_description.split(':', 1)[-1])
                print(reading)

                #set up our embed
                embed = discord.Embed(colour=discord.Colour.green(), title="your tarot card", description="here is a keyword description of your card.")
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
                embed.add_field(name="your card:", value=card, inline=False)
                embed.add_field(name="the card's keyword description:", value=reading, inline=False)
                embed.set_image(url="https://drive.google.com/file/d/11V1aGl6VZX1L5r0PXEoy0mi6p7srHgTH/view?usp=share_link")
                embed.set_footer(text="here are some reaction options")

    #send message with the full reading as embed.   
                await ctx.send(embed=embed)

##daily card pull
@grimalkin.command()
#add cooldown so you can only pull once a day...we will add an error handler below in start-up loads
@commands.cooldown(1, 43200, commands.BucketType.user)
async def daily(ctx, author):
    with open("card.txt", "r") as file1:
        card_options=file1.read().splitlines()
        response_card=random.choice(card_options)
        card=str(response_card)
        print(card)

    with open("description.txt", "r") as file2:
        descriptions=file2.readlines()
        for line in descriptions:
            if line.startswith(card):
                card_description=str(line)
                reading=(card_description.split(':', 1)[-1])
                print(reading)

                embed = discord.Embed(colour=discord.Colour.green(), title="your tarot card", description="here is a keyword description of your card.")
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
                embed.add_field(name="your card:", value=card, inline=False)
                embed.add_field(name="the card's keyword description:", value=reading, inline=False)
                embed.set_image(url="https://drive.google.com/file/d/11V1aGl6VZX1L5r0PXEoy0mi6p7srHgTH/view?usp=share_link")
                embed.set_footer(text="here are some reaction options")
  
                await ctx.send(embed=embed)

##let's try a past present future reading!
@grimalkin.command()
async def ppf(ctx, author, question):
    #open up the card.txt file, split into lines, and grab random card
    with open("card.txt", "r") as file1:
        card_options=file1.read().splitlines()
        card_1=random.choice(card_options)
        card_2=random.choice(card_options)
        card_3=random.choice(card_options)
        cards = [card_1, card_2, card_3]

        for your_cards in cards:
            if card_1 == card_2:
                del card_1
                card_1=random.choice(card_options)

            if card_1 == card_3:
                del card_1
                card_1=random.choices(card_options)

            if card_2 == card_3:
                del card_2
                card_2=random.choice(card_options)

            if card_1!=card_2 and card_1!=card_3 and card_2!=card_3:
                print(card_1, card_2, card_3)

            else:
                print("strange...we don't have that card.")
                
            
    with open("upright.txt", "r") as file2, open("reversed.txt", "r") as file3:
        uprights=file2.readlines()
        reverseds=file3.readlines()
        card1=str(card_1)
        card2=str(card_2)
        card3=str(card_3)
        reversed_check="reversed"
        #match card 1's description
        for line in reverseds:
             if card1 in line:
                desc_1=str(line)
                desc1=desc_1.split(':', 1)[-1]
                print("desc_1 = "+desc_1)
                break
             for line in uprights:
                if (card1+" : ") in line:
                    desc_1=str(line)
                    desc1=desc_1.split(':', 1)[-1]
                    print("desc_1 = "+desc_1)
                break
             else:
                 print("card1 not found in any directory.")
                 break
         
        #match card 2's description
        for line in reverseds:
             if card2 in line:
                desc_2=str(line)
                desc2=desc_2.split(':', 1)[-1]
                print("desc_2 = "+desc_2)
                break
             for line in uprights:
                if (card2+" : ") in line:
                    desc_2=str(line)
                    print("desc_2 = "+desc_2)
                    desc2=desc_2.split(':', 1)[-1]
                break
             else:
                 print("card2 not found in any directory.")
                 break
        
        #match card 3's description
        for line in reverseds:
             if card3 in line:
                desc_3=str(line)
                print("desc_3 = "+desc_3)
                desc3=desc_3.split(':', 1)[-1]
                break
             for line in uprights:
                if (card2+" : ") in line:
                    desc_3=str(line)
                    print("desc_3 = "+desc_3)
                    desc3=desc_3.split(':', 1)[-1]
                break   
             else:
                 print("card3 not found in any directory.")
                 break
    #set variables able to be used by embed function

    embed = discord.Embed(colour=discord.Colour.green(), title="your past present future reading", description="here are keyword descriptions of your cards.")
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.add_field(name="your cards", value=(card1+"\n"+card2+"\n"+card3+"\n"), inline=False)
    embed.add_field(name="your past, present, and future reading", value=("your past had themes of : "+desc1+"\n"+"your present has themes of : "+desc2+"\n"+"your future will have themes of : "+desc3+"\n"), inline=False)
    embed.set_image(url="https://drive.google.com/file/d/11V1aGl6VZX1L5r0PXEoy0mi6p7srHgTH/view?usp=share_link")
    embed.set_footer(text="here are some reaction options")
  
    await ctx.send(embed=embed)

#start-up loads
##new error handler for daily pull
@grimalkin.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('you can only pull a daily card once a day!')
   
@grimalkin.event 
async def on_ready():
    print("grimalkin has found the spectral wavelength")
    change_status.start()

#final run --- do NOT put anything under here
grimalkin.run(token)
####################pip####################