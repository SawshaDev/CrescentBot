from io import BytesIO
import aiohttp
import crescent
import hikari
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)
load_dotenv()

class CrescentBot(crescent.Bot):
    """The base bot class for CrescentBot"""
    def __init__(self):
        super().__init__(token=os.environ['TOKEN'], intents=hikari.Intents.ALL)
        self.subscribe(hikari.StartedEvent, self.on_start)
        self.subscribe(hikari.StoppingEvent, self.on_close)

    async def on_start(self, _: hikari.StartedEvent) -> None:
        self.session = aiohttp.ClientSession()
        self.plugins.load_folder('modules')
        for plugin in self.plugins.plugins:
            logger.warning(f"Loaded {plugin}!")      

    async def on_close(self,  _: hikari.StoppedEvent) -> None:
        await self.session.close()     
        
    async def make_icon(self, icon_url: str):
        """helper function to make a icon url into bytes"""
        async with self.session.get(f"{icon_url}") as resp:
            image = await resp.read()

        return image