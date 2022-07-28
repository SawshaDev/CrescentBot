import hikari
import lightbulb
from bot import CrescentBot
import utils

info = utils.Plugin("info", "everything info wise")


@info.command()
@lightbulb.option("user", "user to get info on", type=hikari.Member, required=False)
@lightbulb.command("userinfo", "Gets info about an user", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def userinfo(ctx: utils.SlashContext, user: hikari.Member):
    user = user or ctx.member
    embed = hikari.Embed()
    embed.add_field(name="Joined date", value=utils.date(user.joined_at, ago=True))
    await ctx.respond(embed=embed, flags=hikari.MessageFlag.EPHEMERAL)
        


def load(bot: CrescentBot):
    bot.add_plugin(info)
    
def unload(bot: CrescentBot):
    bot.remove_plugin(info)