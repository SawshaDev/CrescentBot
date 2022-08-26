import asyncio
import hikari
import lightbulb

from core.bot import CrescentBot

import miru
import utils


bot = CrescentBot()
miru.load(bot)


bot.run()