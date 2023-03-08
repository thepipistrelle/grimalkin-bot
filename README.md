# grimalkin-bot
tarot bot.

@grimalkin.command()
async def ping(ctx):
    embed = discord.Embed(colour=discord.Colour.green(), description="this is the description", title="this is the title")
    
    embed.set_footer(text="this is the footer")
    embed.set_author(name=ctx.message.author, icon_url="https://tenor.com/bpfoU.gif")
    embed.set_thumbnail(url="https://tenor.com/bpfoU.gif")
    embed.set_image(url="https://tenor.com/bpfoU.gif")

    embed.add_field(name="field 1 inline=f", value="https://tenor.com/bpfoU.gif", inline=False)
    embed.add_field(name="field 2 inline=t", value="https://tenor.com/bpfoU.gif", inline=True)
    embed.insert_field_at(1, name="embed.insert_field_at(1,...)", value="https://tenor.com/bpfoU.gif")

    await ctx.send(embed=embed)