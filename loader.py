from aiogram import Bot, Dispatcher, Router
from keys import TOKEN


router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)
