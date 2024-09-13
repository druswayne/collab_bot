from panda3d_tools import text_stats

from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command,Text

@dp.message(F.text == 'привет')
async def func_name_1(message: Message):

    await message.answer(message.text)


@dp.message(F.text =='что приготовить')
async def func_name_2(message: Message):
    list_product = 'рецепт 1\nрецепт 2\nрецепт 3\nрецепт 4\nотправь слово рецепт и номер рецепта'
    await message.answer(text=list_product)

@dp.message(Text(startswith='рецепт '))
async def func_name_2(message: Message):
    list_product = '.рецепт 1\n2.рецепт 2\n3.рецепт 3\n4.рецепт 4'
    text = int(message.text.split()[1])
    if text == 1:
        recept = 'рецепт СИННАБОНОВ\nчто нам надо:\n-МОЛОКО 300 мл\n-ДРОЖЖИ 5 г\n-САХАР много  г\n-МУКА 500 г\n-ЯЙЦА 2 шт\n-ЩЕПОТКА СОЛИ\n-МАСЛО РАСТИТЕЛЬНОЕ 100 г\n-КОРИЦА\nход действий:\n|сперва берем миску и наливаем в нее молоко, добавляем|    |дрожжи,ложку сахара,щепотку соли,перемешиваем, потом|    |накрывем пленкой и ставим в теплое место на час где-то  |    |чтобы наша ОПАРА поднялась|ТЕПЕРЬ добавляем в нашу опару яйца, масло, +-450 г муки.\nЗАМЕШИВАЕМ тесто и оставляем его на час. обминаем и раскатываем чтобы получился большой прямоугольник.\nСМЕШИВАЕМ сахар с корицей(в отдельной миске) и рассыпаем по тесту равномерно. Закручиваем в рулет и разрезаем на отдельные синнабоны.\n В ДУХОВКУ, разогретую до 180 на 25-30 мин\nПРИЯТНОГО АППЕТИТА'

    elif text == 2:
        recept = 'пока не написан'

    elif text == 3:
        recept = 'пока не написан'

    elif text == 4:
        recept = 'пока не написан'

    await message.answer(text=recept)