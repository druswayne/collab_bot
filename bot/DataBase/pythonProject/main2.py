import sqlite3
con = sqlite3.connect("ЗАДАНИЕ 3.db")
cursor = con.cursor()
a = input("введите форму")
cursor.execute('SELECT form FROM medicines WHERE name = (?)', (a,))
print(cursor.fetchall())