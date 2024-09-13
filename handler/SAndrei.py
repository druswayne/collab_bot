from gettext import textdomain

from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command
from aiogram import types

'''@dp.message(Command('delmes'))
async def func_name_2(message: Message, bot:Bot, msg:Message):
 copied_message = await bot.copy_message(chat_id=message.chat.id,
                                            from_chat_id=message.chat.id, message_id=msg_id)
    await bot.delete_message(chat_id=,message_id=)'''

@dp.message(Command('delmes'))
async def test(message: types.message):
       msg = await message.answer('Fmessage')
       await message.answer('Smessage')
       await msg.delete()