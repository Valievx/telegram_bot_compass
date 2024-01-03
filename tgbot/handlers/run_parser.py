from tgbot.services.parser import Parser


async def run_parser(bot):
    client = Parser(bot)
    await client.pars()
