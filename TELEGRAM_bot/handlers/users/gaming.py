from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from loader import router
from aiogram import F, types, Bot
from loader import con, cursor
from keys.key import kb_game

@router.callback_query(F.data.startwith('bet'))
async def game(callback: types.CallbackQuery, bot: Bot):
    bet = int(callback.data.split('_')[1])
    id_user = callback.message.chat.id
    cursor.execute('SELECT money FROM money_table where id=(?)', [id_user])
    money = cursor.fetchall()[0][0]
    if bet>money:
        await callback.answer(text="Недостаточно средств на счету!")
    else:
        await callback.answer(text="Ставка принята!")
        dice_mess = await callback.answer_dice(emoji='🎰')
        value_dice = dice_mess.dice.value
        if value_dice < 30:
           await callback.answer(text="К сожалению ты проиграл")
           #cursor.execute('UPDATE money_table SET  where id=(?)', [id_user])
           money = cursor.fetchall()[0][0]
        else:
           await callback.answer(text=f"Твой выигрыш составил {value_dice}")