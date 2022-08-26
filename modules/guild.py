import hikari
from core.bot import CrescentBot
import utils
import lightbulb

guild = utils.Plugin("guild", "Guild specific commands")

@guild.command()
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.command("roles", "All server roles")
@lightbulb.implements(lightbulb.SlashCommand)
async def roles(ctx: utils.SlashContext):
    guild = ctx.get_guild()
    roles = [guild.get_role(role) for role in guild.get_roles()]
    
    roles = ''.join(f"\n{role.name} ({role.id})" for role in roles)
    await ctx.respond(f"```py\n{roles}```")


def load(bot: CrescentBot):
    bot.add_plugin(guild)

def unload(bot: CrescentBot):
    bot.remove_plugin(guild)