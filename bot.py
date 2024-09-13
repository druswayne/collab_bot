import logging
import asyncio
from tkinter.messagebox import Message

from loader import *
import handler

async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())



