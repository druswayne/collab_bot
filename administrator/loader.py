from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN
import sqlite3

con = sqlite3.connect("data.db")
cursor = con.cursor()

admin_id = 1583624575
FORBIDDEN_WORDS = [
    'спам',
    'реклама',
    'взлом',
]
user_violations = {}
MAX_VIOLATIONS = 3
MUTE_DURATION = 10

router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)