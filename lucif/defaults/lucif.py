from discord.ext import commands
import discord
from cogwatch import watch

class Lucif(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = ".",
            intents = discord.Intents.all(),
            allowed_mentions = discord.AllowedMentions(
                users=False,         # disables ping for all types of mentions
                everyone=False,      # to prevent a poo poo stinky eval leak
                roles=False,         
                replied_user=False,  
            )
        )

    @watch(path='cogs')
    async def on_ready(self):
        print('Bot ready.')

    async def on_message(self, message):
        if message.author.bot: # make bot not respond to its own message,
            return # preventing of course command recursion

        await self.process_commands(message)

