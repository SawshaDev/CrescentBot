from io import BytesIO
import aiohttp
import lightbulb
import hikari
from dotenv import load_dotenv
import os

load_dotenv()

class CrescentBot(lightbulb.BotApp):
    def __init__(self):
        super().__init__(token=os.environ['TOKEN'], intents=hikari.Intents.ALL, prefix="c!")
        self.subscribe(hikari.StartedEvent, self.on_start)
        self.subscribe(hikari.StoppedEvent, self.on_close)

    async def on_start(self, _: hikari.StartedEvent) -> None:
        self.session = aiohttp.ClientSession()
        self.load_extensions("lightbulb.ext.filament.exts.superuser")
        exts = [
            f"modules.{ext if not ext.endswith('.py') else ext[:-3]}"
            for ext in os.listdir("modules")
            if not ext.startswith("_")
        ]
        for ext in exts:
            self.load_extensions(ext)
    

    async def on_close(self,  _: hikari.StoppedEvent) -> None:
        await self.session.close()
        

    async def make_icon(self, icon_url: str):
        """helper function to make a guild icon url into bytes"""

        async with self.session.get(f"{icon_url}") as resp:
            image = BytesIO(await resp.read())

        return image