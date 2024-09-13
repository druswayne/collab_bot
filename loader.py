from aiogram import Bot, Dispatcher, Router

TOKEN = '7309473238:AAFFAinUM7Fddsdi13MKyT_qXnnfIs_vtsU'
router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)
