from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN
import sqlite3

con = sqlite3.connect("data/violation_for_users.db")
cursor = con.cursor()

admin_id = 1583624575

with open(f'data/words.txt', 'r', encoding='utf-8') as file:
    FORBIDDEN_WORDS = file.read().split()
print(FORBIDDEN_WORDS)

cursor.execute('SELECT id FROM viol')
user_violations = cursor.fetchall()

MAX_VIOLATIONS = 3
MUTE_DURATION = 10

router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)