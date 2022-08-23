import crescent
from utils import Context, Plugin
import hikari
import logging


plugin = Plugin() 
logger = logging.getLogger(__name__)


@plugin.include
@crescent.command
async def idk(ctx: Context):
    resp = await ctx.session.get("https://sawsha-is.gay/2MxCasXq8.png/")

    await ctx.respond(attachment=await resp.read())

@plugin.load_hook
def on_load() -> None:
    logger.info("Loaded")

@plugin.unload_hook
def on_unload() -> None:
    logger.info("Unloaded")