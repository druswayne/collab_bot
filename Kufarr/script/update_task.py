from loader import cursor, bot, scheduler, con
from script.parser import parser_update
from aiogram.types import Message


def updating():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        id_user = user[0]
        task = scheduler.add_job(parser_update,
                                 trigger='interval',
                                 seconds=10,
                                 kwargs={'user_id': id_user, 'bot': bot})
        cursor.execute('UPDATE users SET id_task=(?) WHERE id=(?)', [task.id, id_user])
        con.commit()