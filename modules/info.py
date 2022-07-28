from io import BytesIO
import random
import hikari
import lightbulb
from bot import CrescentBot
import utils
from lightbulb.ext import tasks

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

@info.command()
@lightbulb.option("guild", "A server to get info on", required=False)
@lightbulb.command("serverinfo", "gets info on a server", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def serverinfo(ctx: utils.SlashContext, guild=None):
    if guild is None:
        guild = ctx.get_guild()
    
    
    try:
        guild = await ctx.bot.rest.fetch_guild(guild)
    except hikari.ForbiddenError:
        await ctx.respond(f"I do not have access to the guild: {guild}!")


    guild_icon = await ctx.bot.make_guild_icon(guild.icon_url)
    
    
    

    await ctx.respond(f"Info on {guild.name} ({guild.id})", attachment=guild_icon,flags=hikari.MessageFlag.EPHEMERAL)


    


@tasks.task(m=5)
async def ch_pr():
    guilds = len([guild for guild in info.bot.cache.get_guilds_view()])
    await info.bot.update_presence(activity=hikari.Activity(type=hikari.ActivityType.PLAYING, name=f"in {guilds} servers!"))


def load(bot: CrescentBot):
    
    ch_pr.start()
    bot.add_plugin(info)
    
def unload(bot: CrescentBot):
    ch_pr.stop()
    bot.remove_plugin(info)