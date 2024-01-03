import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import keyboard as kb
from tgbot.config import load_config
from tgbot.handlers.run_parser import run_parser

# Configure logging
logging.basicConfig(level=logging.INFO)

# Загружаем конфиг
config = load_config('.env')

bot = Bot(token=config.bot.token, parse_mode=config.bot.parse_mode)
dp = Dispatcher(bot)
bot.config = config


async def main():
    # Запускаем бота параллельно с циклом парсера
    try:
        print(f'Bot {config.bot.name} {config.bot.version} started!')
        await asyncio.gather(
            dp.start_polling(),
            run_parser(bot)
        )
    finally:
        await bot.get_session()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    with open('./menu.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo,
                             'Compass - поможет Вам следить за сообщениями '
                             'связанными с вашими интересами 💬\n\n'
                             'Нахожу сообщения и тут же отправляю их тебе 🔥 ',
                             reply_markup=kb.menu)

if __name__ == '__main__':
    try:
        asyncio.run(main()),
        send_welcome()
    except (KeyboardInterrupt, SystemExit):
        print(f'Bot stopped!')
