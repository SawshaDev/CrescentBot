import hikari
import lightbulb
import utils
from lightbulb.ext import tasks
from .view import BasicView
from typing import Optional

info = utils.Plugin("info", "everything info wise")



@info.command()
@lightbulb.option("user", "user to get info on", type=hikari.Member, required=False)
@lightbulb.command("userinfo", "Gets info about an user", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def userinfo(ctx: utils.SlashContext, user: Optional[hikari.Member]):
    user = user or ctx.member
    view = BasicView(ctx, user)  # Create an instance of our newly created BasicView

    embed = hikari.Embed(description=f"Info about {user.mention}")

    message = await ctx.respond(embed=embed,
        components=view.build()
    )
    view.start(await message.message())  # Start listening for interactions

    await view.wait()  # Wait until the view is stopped or times out



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
        await ctx.respond(f"I do not have access to the {guild.name}!")


    guild_icon = await ctx.bot.make_icon(guild.icon_url) if guild.icon_url is not None else "https://cdn.discordapp.com/embed/avatars/1.png"
    
    
    await ctx.respond(f"Info on {guild.name} ({guild.id})", attachment=guild_icon,flags=hikari.MessageFlag.EPHEMERAL)




@tasks.task(m=5)
async def ch_pr():
    guilds = len([guild for guild in info.bot.cache.get_guilds_view()])
    await info.bot.update_presence(activity=hikari.Activity(type=hikari.ActivityType.PLAYING, name=f"in {guilds} servers!"))

