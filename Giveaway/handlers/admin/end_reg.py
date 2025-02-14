from aiogram.types import Message
from aiogram.filters import Command
from loader import router, cursor, con, admin_id

@router.message(Command('end_reg'))
async def fun_start(message: Message):
    id_user = message.chat.id
    if id_user != admin_id:
        await message.answer(text="Нет доступа")
    else:
        cursor.execute("UPDATE start_reg SET status = False")
        con.commit()
        await message.answer(text="Регистрация конкурса закрыта")