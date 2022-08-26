from core.bot import CrescentBot
import lightbulb
import typing as t

class Plugin(lightbulb.Plugin):
    @property
    def bot(self) -> CrescentBot:
        return t.cast(CrescentBot, self.app)

class Context(lightbulb.Context):
    @property
    def bot(self) -> CrescentBot:
        return t.cast(CrescentBot, self.app)

class SlashContext(lightbulb.SlashContext, Context):
    ...

class PrefixContext(lightbulb.PrefixContext, Context):
    ...