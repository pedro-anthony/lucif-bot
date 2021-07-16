from discord.ext import commands
import discord

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='bubbles'
    )
    async def bubbles(self, ctx):
        data = await self.ensure_data(ctx.author.id)
        if data:
            embed = discord.Embed(
                title="Here you go, you fucking tard.",
                description=f"$: {data['bubbles']}",
                colour=0x00aeff
            )
            await ctx.send(embed=embed)

    async def ensure_data(self, object_id: int):
        data = await self.bot.economy.find(object_id)
        if data:
            return data
        else:
            await self.bot.economy.insert({"_id": object_id, "bubbles": 0})


    @commands.command(
        name='pay'
    )
    async def pay(self, ctx, lucky_man: discord.Member, amount:int):
        self_crumbs = await self.ensure_data(ctx.author.id)
        other_crumbs = await self.ensure_data(lucky_man.id)
        if self_crumbs['bubbles'] >= amount:
            await self.bot.economy.increment(ctx.author.id, -amount, "bubbles")
            await self.bot.economy.increment(lucky_man.id, amount, "bubbles")
            await ctx.send("Done!")
        else:
            await ctx.send("You broke ass bitch, you ain't got that kinda cash.")


def setup(bot):
    bot.add_cog(Economy(bot))