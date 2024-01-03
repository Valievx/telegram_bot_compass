from aiogram import types

menu = types.InlineKeyboardMarkup(row_width=1)
menu.add(
    types.InlineKeyboardButton('📩Получить сообщения📩', callback_data='parse'),
    types.InlineKeyboardButton('🚩Остановить🚩', callback_data='stop')
)
