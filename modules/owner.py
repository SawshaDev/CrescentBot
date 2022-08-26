import hikari
import lightbulb
import utils
from core.bot import CrescentBot

owner = utils.Plugin("owner", "owner only commands")

@owner.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option("module", "The module to reload", modifier=lightbulb.OptionModifier.CONSUME_REST)
@lightbulb.command("reload", "reloads a module", pass_options=True)
@lightbulb.implements(lightbulb.PrefixCommand)
async def reload(ctx: utils.PrefixContext, module):
    try: 
        ctx.bot.reload_extensions(module)
        return await ctx.respond(f"Reloaded {module}")
    except Exception as e:
        return await ctx.respond(f"There was an error!\nError Type: {e.__class__.__name__}\n```py\n{e}```")


def load(bot: CrescentBot):
    bot.add_plugin(owner)


def unload(bot: CrescentBot):
    bot.remove_plugin(owner)
