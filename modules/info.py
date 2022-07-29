from io import BytesIO
import random
import hikari
import lightbulb
from bot import CrescentBot
import utils
from lightbulb.ext import tasks
import miru

info = utils.Plugin("info", "everything info wise")

class SelectStuff(miru.Select):
    def __init__(self, ctx: miru.Context, member: hikari.Member):
        self.ctx = ctx
        self.member = member

        options = [
            miru.SelectOption(label="avatar"),
            miru.SelectOption(label="close", emoji=f"\N{BLACK SQUARE FOR STOP}")
        ]
        super().__init__(placeholder="Choose userinfo", options=options)

    async def callback(self,ctx: miru.Context):
        if self.values[0] == "close":
            for item in ctx.view.children:
                if isinstance(item, miru.Select):
                    item.disabled=True

            await ctx.edit_response(components=self.view.build())
            await ctx.respond("Closed select")

        if self.values[0] == "avatar":
            embed = hikari.Embed()
            embed.set_image(self.member.avatar_url)

            return await ctx.edit_response(embed=embed, components=ctx.view.build())


class BasicView(miru.View):
    def __init__(self, ctx, member: hikari.Member):
        self.ctx = ctx
        super().__init__(timeout=None)
        self.add_item(SelectStuff(ctx, member))


@info.command()
@lightbulb.option("user", "user to get info on", type=hikari.Member, required=False)
@lightbulb.command("userinfo", "Gets info about an user", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def userinfo(ctx: utils.SlashContext, user: hikari.Member):

    user = user or ctx.member
    view = BasicView(ctx, user)  # Create an instance of our newly created BasicView

    message = await ctx.respond(
        "This is a basic component menu built with miru!", components=view.build()
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