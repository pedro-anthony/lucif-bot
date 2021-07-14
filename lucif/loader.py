from lucif.defaults import lucif
import asyncio
from dotenv import load_dotenv
import os

def run():
    load_dotenv()
    bot = lucif.Lucif()
    bot.run(os.environ['TOKEN'])