from aiogram import types

kb_start = [
    types.KeyboardButton(text='Играем!'),
    types.KeyboardButton(text='Меню!')
]

kb_game = [
    types.InlineKeyboardButton(text="Ставка 10$", callback_data="bel_10"),
    types.InlineKeyboardButton(text="Ставка 20$", callback_data="bel_20"),
    types.InlineKeyboardButton(text="Ставка 50$", callback_data="bel_50"),
    types.InlineKeyboardButton(text="Ставка 100$", callback_data="bel_100"),
]