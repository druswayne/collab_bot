import sqlite3
con = sqlite3.connect("data.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS movies
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                rate REAl,
                year INTEGER DEFAULT 0,
                director TEXT,
                gunre TEXT)
            """)
cursor.execute("INSERT INTO movies (name, rate, year, director, gunre) VALUES ('Побег из Шоушенко', 9.3, 1994, 'Фрэнк Дарабонт', 'драма'), ('Крестный отец', 9.2, 1972, 'Фрэнсис Форд Кополла', 'драма'), ('Тёмный рыцарь', 9.0, 2008, 'Кристофер Нолан', 'боевик')")
con.commit()