from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start
from loader import router, cursor, con, scheduler
from aiogram import F

@router.message(F.text == 'Удалить ссылку')
async def fun_start(message: Message):
    id_user = message.chat.id
    cursor.execute('SELECT * FROM users where id=(?)', [id_user])
    data2 = cursor.fetchall()
    if not data2:
        builder = ReplyKeyboardBuilder()
        for button in kb_start:
            builder.add(button)
        builder.adjust(1)
        await message.answer(text='Вы не добавили ссылку', reply_markup=builder.as_markup(resize_keyboard=True))
    else:
        id_task = data2[0][2]
        scheduler.remove_job(id_task)
        cursor.execute('DELETE FROM users where id=(?)', [id_user])
        con.commit()
        builder = ReplyKeyboardBuilder()
        for button in kb_start:
            builder.add(button)
        builder.adjust(1)
        await message.answer(text="Вы удалили ссылку!", reply_markup=builder.as_markup(resize_keyboard=True))