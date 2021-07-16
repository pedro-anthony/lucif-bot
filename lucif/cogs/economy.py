from discord.ext import commands

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='bubbles'
    )
    async def bubbles(self, ctx):
        data = await self.bot.economy.find(ctx.author.id)
        if data:
            await ctx.send(data)
        else:
            await self.bot.economy.insert({"_id": ctx.author.id, "bubbles": 0})
            await ctx.send('It appears you did not have an entry in the database, so one has been created for you. Please re-run the command.')

def setup(bot):
    bot.add_cog(Economy(bot))