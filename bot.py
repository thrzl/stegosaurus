from sys import stdout
import discord
from discord.ext import commands, tasks
import logging
import itertools

logging.basicConfig(
    level=logging.INFO,
    format="S | [%(asctime)s] %(message)s",
    handlers=[logging.StreamHandler(stdout)],
)
logger = logging.getLogger()

intents = discord.Intents.default()

class Help(commands.MinimalHelpCommand):
    def get_opening_note(self):
        return super().get_opening_note().lower()

    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page,color = self.context.bot.color)
            await destination.send(embed=emby)

    def get_command_signature(self, command):
        string = '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)
        return string.lower()

    def add_bot_commands_formatting(self, commands, heading):
        if commands:
            joined = '\u2002'.join(c.name.lower() for c in commands)
            self.paginator.add_line('__**%s**__' % heading)
            self.paginator.add_line(joined)

    async def send_bot_help(self, mapping):
        ctx = self.context
        bot = ctx.bot

        if bot.description:
            self.paginator.add_line(bot.description, empty=True)

        note = self.get_opening_note()
        if note:
            self.paginator.add_line(note, empty=True)

        no_category = 'other'
        def get_category(command, *, no_category=no_category):
            cog = command.cog
            return cog.qualified_name.lower() if cog is not None else no_category

        filtered = await self.filter_commands(bot.commands, sort=True, key=get_category)
        to_iterate = itertools.groupby(filtered, key=get_category)

        for category, commands in to_iterate:
            commands = sorted(commands, key=lambda c: c.name) if self.sort_commands else list(commands)
            self.add_bot_commands_formatting(commands, category)

        note = self.get_ending_note()
        if note:
            self.paginator.add_line()
            self.paginator.add_line(note)

        await self.send_pages()

class Stegosaurus(commands.Bot):
    def __init__(self, command_prefix, description=None, **options):
        super().__init__(
            command_prefix,
            help_command=Help(),
            description=description,
            **options,
        )
        self.member_count = 0
        self.refresh_member_count.start()
        self.color = 0x5000FB

    def load_extension(self, name):
        logger.info(f"loaded {name}")
        return super().load_extension(name)

    @tasks.loop(minutes=5, reconnect=True)
    async def refresh_member_count(self):
        self.member_count = 0
        for i in self.guilds:
            self.member_count += i.member_count


client = Stegosaurus(
    command_prefix=commands.when_mentioned_or("stego ", "stegosaurus ", "s "),
    intents=intents,
    case_insensitive=True,
)


@client.event
async def on_ready():
    logger.info(f"signed in as {client.user.name}")
    logger.info(f"id: {client.user.id}")
    logger.info(
        f"can see {len(client.guilds)} servers and {client.member_count} server members."
    )


@client.event
async def on_command(ctx):
    logger.info(f"{ctx.author.id} used command {ctx.command.name.lower()}.")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    logger.error(f"error {error} occurred in {ctx.command.name.lower()}")
    raise error


@client.command()
@commands.is_owner()
async def reload(ctx: commands.Context, cog):
    message = f"loaded `{cog}` successfully."
    try:
        client.unload_extension(f"cogs.{cog}")
        message = f"cog {cog} reloaded successfully."
    except commands.ExtensionNotLoaded:
        pass
    except Exception as e:
        return await ctx.send(e)
    try:
        client.load_extension(f"cogs.{cog}")
    except commands.ExtensionFailed as e:
        return await ctx.send(str(e).lower())
    return await ctx.send(message)


client.load_extension("cogs.zero")
client.load_extension("cogs.crypt")
client.load_extension("cogs.security")
client.load_extension("jishaku")
client.run("token")
