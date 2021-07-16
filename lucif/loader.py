from lucif.defaults import lucif
import asyncio
from dotenv import load_dotenv
import os
from lucif.utils.mongo import Document
from motor import motor_asyncio

def run():
    load_dotenv()
    bot = lucif.Lucif()
    bot.load_extension('jishaku')
    os.environ['JISHAKU_NO_UNDERSCORE'] = 'True'
    for cog in os.listdir('lucif/cogs'):
        if not cog.startswith('__') and cog.endswith('.py'):
            try:
                bot.load_extension(f'lucif.cogs.{cog[:-3]}')
                print(f'Loaded {cog[:-3]} in.')
            except Exception as err:
                raise err

    bot.mongo = motor_asyncio.AsyncIOMotorClient(str(os.environ['MONGO']))
    bot.db = bot.mongo["lucifdb"]
    bot.economy = Document(bot.db, "economy")

    bot.run(os.environ['TOKEN'])