import sqlite3
con = sqlite3.connect("ЗАДАНИЕ 4.db")
cursor = con.cursor()
cursor.execute('SELECT бренд FROM t_shirts WHERE размер = "L" AND цена<=100 AND цвет != "красный"')
print(cursor.fetchall())