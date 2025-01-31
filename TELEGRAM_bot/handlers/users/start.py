from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start
from loader import router
from loader import con, cursor


@router.message(Command('start'))
async def fun_start(message: Message):
    id_user = message.chat.id
    cursor.execute('SELECT id FROM money_table where id=(?)',[id_user])
    data = cursor.fetchall()
    if not data:
        cursor.execute('INSERT INTO money_table (id) VALUES (?)', [id_user])
        con.commit()
    builder = ReplyKeyboardBuilder()
    for button in kb_start:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text="Добро пожаловать!", reply_markup=builder.as_markup(resize_keyboard=True))
