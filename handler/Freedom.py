from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command


@dp.message(F.text == 'Расскажи шутку')
async def func_name_1(message: Message):
    """
    обработчик, который реагирует на текст "Почему нельзя драться с беременными? Они всегда готовы к схваткам"
    """
    await message.answer(message.text)


@dp.message(Command('joke1'))
async def func_name_2(message: Message):
    """
    обработчик, который реагирует на команду /joke1
    """
    await message.answer(text='Почему нельзя драться с беременными женщинами? Они всегда готовы к схваткам!')


    @dp.message(Command('joke2'))
    async def func_name_3(message: Message):
        """
        обработчик, который реагирует на команду /joke2
        """
        await message.answer(text='Сидят мужики и пьют пиво. Вдруг один из них достаёт из кармана маленького мужичка, наливает ему в напёрсток пиво и говорит: Ну Петрович, расскажи мужикам, как ты в пустыне колдуна на*** послал.')


    @dp.message(Command('joke3'))
    async def func_name_4(message: Message):
        """
        обработчик, который реагирует на команду /joke3
        """
        await message.answer(text='Встречаются двое сталкеров, ну и один говорит:'
                              ' — На днях к Долгу заходил…'
                              ' — Ну и? (спрашивает)'
                              ' — Чо и? (недовольный) И остался должен. Ха. А потом зашел к Свободе…'
                              ' — Ну и чо?'
                              ' — И стал СВОБОДЕН!')


