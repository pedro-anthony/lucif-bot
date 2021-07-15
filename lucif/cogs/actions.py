from discord.ext import commands
import discord
import aiohttp

BASE_URL = "https://api.waifu.pics/sfw/"

async def return_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL + url) as r:
            if r.status == 200:
                json = await r.json()
                return json['url']
                
class Actions(commands.Cog):
    """Use gifs to express yourself!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hug")
    async def hug(self, ctx, person: discord.Member):
        """Hug someone else."""
        if not ctx.author == person:
            embed = discord.Embed(
                title = " ",
                description = f"**{ctx.author.name}** huggies **{person.name}**",
                color=0x00aeff
            )
            img = await return_image('hug')
            embed.set_image(url=img)
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("You can't hug yourself, dumbass.")

    @commands.command(name="kiss")
    async def kiss(self, ctx, person: discord.Member):
        """Kiss someone else."""
        if not ctx.author == person:
            embed = discord.Embed(
                title = " ",
                description = f"**{ctx.author.name}** kisses **{person.name}**",
                color=0x00aeff
            )
            img = await return_image('kiss')
            embed.set_image(url=img)
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("You can't kiss yourself, dumbass.")

    @commands.command(name="cuddle")
    async def cuddle(self, ctx, person: discord.Member):
        """Cuddle with someone else."""
        if not ctx.author == person:
            embed = discord.Embed(
                title = " ",
                description = f"**{ctx.author.name}** cuddles with **{person.name}**",
                color=0x00aeff
            )
            img = await return_image('cuddle')
            embed.set_image(url=img)
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("You can't like.. cuddle with yourself, dumbass.")

    @commands.command(name="slap")
    async def slap(self, ctx, person: discord.Member):
        """Slap someone else."""
        if not ctx.author == person:
            embed = discord.Embed(
                title = " ",
                description = f"**{ctx.author.name}** slaps **{person.name}**",
                color=0x00aeff
            )
            img = await return_image('slap')
            embed.set_image(url=img)
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Why yould you slap yourself?")

    @commands.command(name="kick")
    async def kick(self, ctx, person: discord.Member):
        """Kick someone else."""
        if not ctx.author == person:
            embed = discord.Embed(
                title = " ",
                description = f"**{ctx.author.name}** kicks **{person.name}**",
                color=0x00aeff
            )
            img = await return_image('kick')
            embed.set_image(url=img)
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("I.. don't think that's possible.")

    @commands.command(name="kill")
    async def kill(self, ctx, person: discord.Member):
        """Kill someone else."""
        if not ctx.author == person:
            embed = discord.Embed(
                title = " ",
                description = f"**{ctx.author.name}** kills **{person.name}**",
                color=0x00aeff
            )
            img = await return_image('kill')
            embed.set_image(url=img)
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Sorry, i have no gifs of suicide to show you.")

def setup(bot):
    bot.add_cog(Actions(bot))