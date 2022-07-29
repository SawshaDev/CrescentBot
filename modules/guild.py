import hikari
from bot import CrescentBot
import utils
import lightbulb

guild = utils.Plugin("guild", "Guild specific commands")

@guild.command()
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.command("roles", "All server roles")
@lightbulb.implements(lightbulb.SlashCommand)
async def roles(ctx: utils.SlashContext):
    guild = ctx.get_guild()
    all_role_ids = [role for role in guild.get_roles()]
    roles = [guild.get_role(role) for role in all_role_ids]
    a = '\n'.join(f"```\n{role.name}, Role Members {len(role)}" for role in roles)

    await ctx.respond(a)


def load(bot: CrescentBot):
    bot.add_plugin(guild)