from discord.ext import commands
import discord
import secrets
import hashlib
import string
import aiofiles

class security(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command('passgen',description="generate a secure password.")
    async def passgen(self, ctx: commands.Context, length=8):
        if length > 25:
            return await ctx.send("That's too long!")
        chars = string.ascii_letters + string.digits + string.punctuation
        pwd = ''.join(secrets.choice(chars) for i in range(length))
        embed=discord.Embed(color=self.bot.color)
        embed.add_field(name="your password",value=f'||`{pwd}`||')

    @commands.command('xkcdpassgen',description="generates an [xkcd style](https://xkcd.com/936/) password")
    async def xkcdpassgen(self, ctx:commands.Context, length=4):
        if length > 15:
            return await ctx.send("That's too long!")
        async with aiofiles.open('words.txt','r') as f:
            words = [word.strip() for word in f]
            pwd = ''.join(secrets.choice(words) for i in range(length))


def setup(bot):
    bot.add_cog(security(bot))