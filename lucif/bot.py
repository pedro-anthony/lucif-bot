from defaults import lucif
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
lucif = lucif.Lucif()

lucif.run(os.environ['TOKEN'])