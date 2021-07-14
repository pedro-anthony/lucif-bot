from discord.ext import commands
import discord
import aiohttp

async def return_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://nekos.life/api/v2/img/{url}') as r:
            if r.status == 200:
                json = await r.json()
                return json['url']
                
class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hug")
    async def hug(self, ctx, person: discord.Member):
        embed = discord.Embed(
            title = " ",
            description = f"**{ctx.author.name}** huggies **{person.name}**",
            color=0x00aeff
        )
        img = await return_image('hug')
        embed.set_image(url=img)
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Actions(bot))