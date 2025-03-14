import logging
import asyncio
from loader import *
from script.update_task import updating

import handlers.users.start
import handlers.users.add
import handlers.users.delete

async def main():
    scheduler.start()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

updating()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())