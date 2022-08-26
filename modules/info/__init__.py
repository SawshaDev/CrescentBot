from .info import info, ch_pr
from core.bot import CrescentBot


def load(bot: CrescentBot):
    ch_pr.start()
    bot.add_plugin(info)
    
def unload(bot: CrescentBot):
    ch_pr.stop()
    bot.remove_plugin(info)