import logging
import hikari
import crescent
from utils import Context, Plugin

plugin = Plugin()
logger = logging.getLogger(__name__)

@plugin.load_hook
def on_load() -> None:
    logger.info(f"Loaded ")

@plugin.unload_hook
def on_unload() -> None:
    logger.info("Unloaded")