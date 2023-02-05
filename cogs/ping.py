import disnake
from disnake.ext import commands

class PingCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        embed = disnake.Embed(
            title="Pong!",
            description=f"Latency: {round(self.bot.latency * 1000)}ms",
            color=0x00FF00,
        )
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))