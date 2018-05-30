import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$', description='A bot that greets the user back.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game("use $help")
    await bot.change_presence(activity=game)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bot", description="Posts hot posts from Reddit.")

    embed.add_field(name="$refresh all", value="Checks for new posts on Reddit.", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('NDUxNDQ3Njg4NDcxMzc5OTY4.DfCDSA.27SkW30lMzLsnJ106yN78zjXuJI')
