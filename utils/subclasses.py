import hikari
import crescent
import aiohttp
import typing as t
from core.bot import CrescentBot


class Context(crescent.Context):
    @property
    def bot(self) -> CrescentBot:
        return t.cast(CrescentBot, self.app)

    @property
    def session(self) -> aiohttp.ClientSession:
        return self.bot.session

class Plugin(crescent.Plugin):
    @property
    def bot(self) -> CrescentBot:
        return t.cast(CrescentBot, self.app)