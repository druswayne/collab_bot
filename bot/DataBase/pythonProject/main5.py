import sqlite3
con = sqlite3.connect("ЗАДАНИЕ 6.db")
cursor = con.cursor()
a = input("введите продукт и его вес: ")
cursor.execute('SELECT calories FROM calories WHERE name = (?)', (a.split()[0],))
print(cursor.fetchall())
print(a)