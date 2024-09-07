from aiogram import Bot, Dispatcher, Router

TOKEN = '7385714840:AAGboUJkVyGK-XD0hdzC54qYsi9OTi9Mygo'
router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)
