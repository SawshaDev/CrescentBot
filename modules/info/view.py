import hikari, miru

class SelectStuff(miru.Select):
    def __init__(self, ctx: miru.Context, member: hikari.Member):
        self.ctx = ctx
        self.member = member
        self.embed = hikari.Embed()

        options = [
            miru.SelectOption(label="avatar"),
            miru.SelectOption(label="banner"),
            miru.SelectOption(label="close", emoji=f"\N{BLACK SQUARE FOR STOP}")
        ]
        super().__init__(placeholder="Choose userinfo", options=options)

    async def callback(self,ctx: miru.Context):
        if self.values[0] == "close":
            for item in ctx.view.children:
                if isinstance(item, miru.Select):
                    item.disabled=True

            await ctx.edit_response("Closed the select! you might need to redo the command for it to re-work!",components=self.view.build())

        if self.values[0] == "avatar":
            self.embed.set_image(self.member.avatar_url)

            return await ctx.edit_response(embed=self.embed, components=ctx.view.build())


        if self.values[0] == "banner":
            user = await ctx.app.rest.fetch_user(self.member)
            print(user.banner_url)
            
            self.embed.set_image(user.banner_url)
            return await ctx.edit_response(embed=self.embed, components=ctx.view.build())

class BasicView(miru.View):
    def __init__(self, ctx, member: hikari.Member):
        self.ctx = ctx
        super().__init__(timeout=None)
        self.add_item(SelectStuff(ctx, member))