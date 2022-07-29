import asyncio
import hikari
import lightbulb
from bot import CrescentBot
import miru
import utils


bot = CrescentBot()
miru.load(bot)



class BasicView(miru.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__(timeout=None)

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True
        
        await self.ctx.edit_last_response(components=self.build())

        print("timeot")

    # Define a new Select menu with two options
    @miru.select(
        placeholder="Select me!", 
        options=[
            miru.SelectOption(label="Option 1"), 
            miru.SelectOption(label="Option 2"),
        ],
    )
    async def basic_select(self, select: miru.Select, ctx: miru.Context) -> None:
        if select.values[0] == "Option 1":
            await ctx.respond(f"a {ctx.user.mention}", user_mentions=True)

    async def view_check(self, ctx: miru.Context) -> bool:

        user = self.ctx.user.id

        print(user == ctx.user.id)

        if ctx.user.id == user:
            return True
        await ctx.respond(f"You cant use this as you're not the command invoker, only the author (<@{user}>) Can Do This!", flags=hikari.MessageFlag.EPHEMERAL)
        return False

    # Define a new Button with the Style of success (Green)
    @miru.button(label="Click me!", style=hikari.ButtonStyle.SUCCESS)
    async def basic_button(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.respond("You clicked me!")

    # Define a new Button that when pressed will stop the view & invalidate all the buttons in this view
    @miru.button(label="Stop me!", style=hikari.ButtonStyle.DANGER)
    async def stop_button(self, button: miru.Button, ctx: miru.Context) -> None:
        for item in self.children:
            item.disabled = True
        
        await ctx.edit_response(components=self.build())

@bot.command()
@lightbulb.command("test", "A")
@lightbulb.implements(lightbulb.PrefixCommand)
async def test(ctx: utils.Context):
            view = BasicView(ctx)  # Create an instance of our newly created BasicView
            # Build the components defined in the view and attach them to our message
            # View.build() returns a list of the built action-rows, ready to be sent in a message
            message = await ctx.respond(
                "This is a basic component menu built with miru!", components=view.build()
            )
            view.start(await message.message())  # Start listening for interactions

            await view.wait()  # Wait until the view is stopped or times out


bot.run()