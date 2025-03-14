from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start
from loader import router, cursor, bot, scheduler, con

@router.message(Command('start'))
async def fun_start(message: Message):
    text = message.text
    text = text.split()
    if len(text)>1:
        FinTok = text[1]
        cursor.execute('SELECT token FROM stats')
        tokens = cursor.fetchall()
        print(tokens)
    builder = ReplyKeyboardBuilder()
    for button in kb_start:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text="Добро пожаловать!", reply_markup=builder.as_markup(resize_keyboard=True))