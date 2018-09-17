import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='ty-')

@bot.event
async def on_ready():
    print('You started the following bot:')
    print(bot.user.name)
    print(bot.user.id)
    print('Bot is online now!')
    print('------------------------------')
    print('If you have any questions with this bot, please ask TYX in Discord. His tag and username is: TYX#9445.')
    print('Created this bot using Python 3.6.')
    print('------------------------------------------------------------------------------------------------------')
    print('Other command scripts will be informed down here:')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send("Hello there! :smiley::wave:")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="TYX's Bot", description="Currently on Beta 2.", color=0x0065ff)
    
    embed.add_field(name="Version", value="1.3.21 Beta")

    embed.add_field(name="Creator", value="TYX#9445")

    # give info about you here
    embed.add_field(name="Bot created in:", value="September 6, 2018")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Servers", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite the bot using this URL!", value="https://discordapp.com/api/oauth2/authorize?client_id=484898327306174475&permissions=8&scope=bot")

    await ctx.send(embed=embed)

@bot.command()
async def windowsbot(ctx):
    await ctx.send("Is **WindowsBot#7625** the bot name and tag you're looking for?")

@bot.command()
async def windowsbotinvite(ctx):
    await ctx.send("Here is the invite link of WindowsBot: https://discordapp.com/oauth2/authorize?client_id=483559421721575426&scope=bot&permissions=2146958591")
    await ctx.send("Make sure to select the correct server when you're adding it!")

@bot.command()
async def tyx(ctx):
    await ctx.send("Here is the link to TYX's YouTube channel:")
    await ctx.send("https://www.youtube.com/channel/UCdagnjhwXhKIgSaEeLA1fLg")

@bot.command()
async def tyxfbr(ctx):
    await ctx.send("Here is the link to TYX's second YouTube channel, TYXFBR:")
    await ctx.send("https://www.youtube.com/channel/UCX7jWblY0qGRD7mMDQNTxDA")

@bot.command()
async def xun(ctx):
    await ctx.send("Here is the link to Xun'sMovies's YouTube channel:")
    await ctx.send("https://www.youtube.com/channel/UC4OVcNt2v_jPCGbl9uo03kg")

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="TYX's Bot", description="Currently on Beta 2. List of commands are:", color=0x0065ff)

    embed.add_field(name="ty-tyx", value="Gives the link to TYX's YouTube channel.", inline=False)
    embed.add_field(name="ty-tyxfbr", value="Gives the link to TYX's second YouTube channel, TYXFBR.")
    embed.add_field(name="ty-xun", value="Gives the link to Xun'sMovies's YouTube channel.", inline=False)
    embed.add_field(name="ty-add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="ty-multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="ty-greet", value="Gives a nice greet message!", inline=False)
    embed.add_field(name="ty-cat", value="Gives a cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="ty-info", value="Gives a little info about the bot.", inline=False)
    embed.add_field(name="ty-help", value="Gives this message.", inline=False)
    embed.add_field(name="ty-windowsbot", value="Gives the username and the tag of WindowsBot.", inline=False)
    embed.add_field(name="ty-windowsbotinvite", value="Gives the invite link of WindowsBot.", inline=False)

    await ctx.send(embed=embed)



bot.run('NDg0ODk4MzI3MzA2MTc0NDc1.DnSo2g.ZO5-2S_Jhn2GXVYGRLB7LCFR4V4')