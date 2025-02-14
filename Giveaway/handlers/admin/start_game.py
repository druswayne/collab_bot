import json
from aiogram.types import Message
from aiogram.filters import Command
from loader import router, cursor, con, admin_id, bot
import random

@router.message(Command('start_game'))
async def fun_start(message: Message):
    id_user = message.chat.id
    if id_user != admin_id:
        await message.answer(text="Нет доступа")
    else:
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        random.shuffle(data)
        with open('data/data.json', encoding='utf-8') as file:
            prize = json.loads(file.read())
        text = ('Розыгрыш завершён!\n'
                'Поздравляем победителей с победой:\n'
                )
        for i in range(1):
            text += f'{data[i][1]} - {prize[i]}\n'
        for user in data:
            try:
                await bot.send_message(text=text, chat_id=user[0])
            except:
                pass
        cursor.execute("DELETE FROM users")
        cursor.execute("UPDATE start_reg SET status = False")
        con.commit()