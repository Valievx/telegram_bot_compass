from datetime import datetime, timedelta
from pyrogram import Client


time = datetime.now() - timedelta(days=2)


class Parser:
    def __init__(self, bot):
        self.client = Client(
            'client',
            api_id=25754771,
            api_hash='9583abf828fa887a61b6d6e61945e0ea'
        )
        self.bot = bot
        self.config = bot.config
        self.data = bot.config.data

    # Читаем последние 10 сообщений в чатах и парсим их
    async def pars(self):
        pars, pars_id, pars_word = await self.data.get_pars_config()
        if not pars:
            return pars
        # Запускаем клиент
        async with self.client as client:
            for i in pars_id:
                # Открываем историю чата
                async for message in client.get_chat_history(int(i)):
                    txt = message.caption if message.caption else message.text
                    # Выводим сообщения за 30 дней
                    if message.date < time:
                        break
                    else:
                        print(message.date, ':', message.chat.title, ':', message.text)

                        chat = await client.get_chat(i)
                        link = (f'<a href="t.me/{message.from_user.username}">{message.from_user.first_name}</>'
                                if message.from_user.username else message.from_user.first_name)
                        text = [
                          f"🔔 <b>{chat.title} | {link}</>\n",
                          txt
                        ]

                    # Отправляем сообщение
                        await self.bot.send_message(self.config.admin, '\n'.join(text), disable_web_page_preview=True)
