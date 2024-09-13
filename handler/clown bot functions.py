import logging
import asyncio
from loader import *
import handler
from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command

async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())







@dp.message(F.text == 'Какие есть анекдоты?')
async def func_name_1(message: Message):

    await message.answer('1-про улитку и бар, 2-про рыбака и удочку')

    @dp.message(F.text == '1')
    async def func_name_1(message: Message):
        await message.answer('Заходит однажды в бар улитка и говорит:-Можно виски с колой?- Простите, но мы не обслуживаем улиток.И бармен вышвырнул ее за дверь.Через неделю заходит опять эта улитка и спрашивает:-Ну и зачем ты это сделал!?')

    @dp.message(F.text == '2')
    async def func_name_1(message: Message):
        await message.answer('я не придумал(')

@dp.message(F.text == 'Клоун привет')
async def func_name_1(message: Message):
    await message.answer('велосипед!')

@dp.message(F.text == 'Бот я хочу шутку')
async def func_name_1(message: Message):
    await message.answer('а она тебя не хочет!')

@dp.message(F.text == 'Кто самый смешной актёр?')
async def func_name_2(message: Message):

    await message.answer('Я. Ну и какой то Ле́сли Уи́льям Ни́льсен ')

@dp.message(Command('викторина'))
async def func_name_2(message: Message):

    await message.answer(text='Что кидают клоуны в лицо?')
    @dp.message(F.text=='банановый пирог')
    async def func_name_2(message: Message):
        await message.answer('Молодец!Кто был первым клоуном?')





        @dp.message(F.text == 'Джозеф Гримальди')
        async def func_name_2(message: Message):
            await message.answer('Всё конец викторины 153478 балов из 153478')
            image = FSInputFile('data/image/1.jpg')

            await message.answer_photo(image)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())