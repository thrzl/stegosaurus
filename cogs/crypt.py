from discord.ext import commands
import discord
import aiohttp
import aiofiles

class crypt(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def caesarenc(self, text: str):
        enc = ''
        for n, i in enumerate(text):
            if i != ' ':
                if i == 'z':
                    nxt = 'a'
                else:
                    nxt = text[n+1]
                enc += nxt
        return enc

    def caesardec(self, text: str):
        enc = ''
        for n, i in enumerate(text):
            if i != ' ':
                if i == 'a':
                    nxt = 'z'
                else:
                    nxt = text[n-1]
                enc += nxt
        return enc

    @commands.command('cencode')
    async def cencode(self, ctx: commands.Context, text):
        nt = self.caesarenc(text)
        embed = discord.Embed(color=self.bot.color)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='your new text',value=f'```{nt}```')
        await ctx.send(embed=embed)

    @commands.command('cdecode')
    async def cdecode(self, ctx: commands.Context, text):
        nt = self.caesardec(text)
        embed = discord.Embed(color=self.bot.color)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='your new text',value=f'```{nt}```')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(crypt(bot))