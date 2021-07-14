from lucif.defaults import lucif
import asyncio
from dotenv import load_dotenv
import os

def run():
    load_dotenv()
    bot = lucif.Lucif()
    for cog in os.listdir('lucif/cogs'):
        if not cog.startswith('__'):
            bot.load_extension(f'lucif.cogs.{cog[:-3]}')
    
    bot.run(os.environ['TOKEN'])