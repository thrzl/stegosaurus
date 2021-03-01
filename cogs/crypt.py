from discord.ext import commands
import discord
import typing

class crypt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 50
        self.a1dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    def caesarenc(self, text: str, key: int):
        enc = ""
        for n, i in enumerate(text):
            if i != " ":
                nxt = self.alphabet[self.alphabet.index(i) + key]
                enc += nxt
        return enc

    def caesardec(self, text: str, key: int):
        enc = ""
        for n, i in enumerate(text):
            if i != " ":
                nxt = self.alphabet[self.alphabet.index(i) - key]
                enc += nxt
        return enc

    @commands.command("cencode", description="encrypt text using caesar cipher.")
    async def cencode(self, ctx: commands.Context, key:typing.Optional[int], text):
        if not key: key = 13
        nt = self.caesarenc(text, key)
        embed = discord.Embed(color=self.bot.color)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="your new text", value=f"```{nt}```")
        embed.set_footer(text="text encryption: caesar cipher")
        await ctx.send(embed=embed)

    @commands.command("cdecode", description="decrypt text using caesar cipher.")
    async def cdecode(self, ctx: commands.Context, key:typing.Optional[int], text):
        if not key: key = 13
        nt = self.caesardec(text, key)
        embed = discord.Embed(color=self.bot.color)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="your new text", value=f"```{nt}```")
        embed.set_footer(text="text decryption: caesar cipher")
        await ctx.send(embed=embed)

    @commands.command("a1encode", description="encrypt text using a1z26.")
    async def a1encode(self, ctx: commands.Context, text):
        nt = ""
        for i in text:
            if i == " ":
                nt += " ,"
                continue
            nt += str(self.a1dict[i]) + ","
        embed = discord.Embed(color=self.bot.color)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="your new text", value=f"```{nt[:-1]}```")
        embed.set_footer(text="text encryption: caesar cipher")
        await ctx.send(embed=embed)

    @commands.command("a1decode", description="decrypt text using a1z26.")
    async def a1decode(self, ctx: commands.Context, text):
        nt = ""
        for i in text.split(","):
            if i == " ":
                nt += " "
                continue
            if not i:
                continue
            for e in self.a1dict.items():
                if e[1] == int(i):
                    nt += e[0]
        embed = discord.Embed(color=self.bot.color)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="your new text", value=f"```{nt}```")
        embed.set_footer(text="text decryption: caesar cipher")
        await ctx.send(embed=embed)

    @commands.command("bencode")
    async def bencode(self, ctx: commands.Context, *, text: str):
        binarystr = ""
        for i in text:
            binarystr += "".join(format(ord(i), "08b") for i in ",".join(text)) + ","
        embed = discord.Embed(color=self.bot.color)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="your text:", value=f"```{binarystr[:-1]}```")
        await ctx.send(embed=embed)

    @commands.command("bdecode")
    async def bdecode(self, ctx: commands.Context, *, text):
        final = ""
        nt = text.split(",")
        for c in nt:
            if len(c) <= 8:
                ntext = c[i : i + 8]
                if i == " ":
                    continue
                final += chr(int(ntext, 2))
            else:
                for i in range(0, len(c), 8):
                    ntext = c[i : i + 8]
                    if i == " ":
                        continue
                    final += chr(int(ntext, 2))
            print(final)
            print(c)
        embed = discord.Embed(color=self.bot.color)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="hidden text:", value=f"```{final}```")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(crypt(bot))