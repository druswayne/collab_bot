from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from loader import router
from aiogram import F, types
from loader import con, cursor
from keys.key import kb_game

@router.message(F.text == 'Играем!')
async def fun_start(message: Message):
    id_user = message.chat.id
    await message.answer("Игра начинается!", reply_markup=types.ReplyKeyboardRemove())
    cursor.execute('SELECT money FROM money_table where id=(?)', [id_user])
    money = cursor.fetchall()[0][0]
    builder = InlineKeyboardBuilder()
    for button in kb_game:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text=f"Ваш баланс: {money}\nДелаем ставку?", reply_markup=builder.as_markup(resize_markup=True))




