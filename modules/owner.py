import hikari
import lightbulb
import utils
from bot import CrescentBot

owner = utils.Plugin("owner", "owner only commands")


def load(bot: CrescentBot):
    bot.add_plugin(owner)