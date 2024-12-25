import sqlite3

# init db
conn = sqlite3.connect("store.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS equipment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_name TEXT UNIQUE NOT NULL,
        nickname TEXT,
        cost REAL NOT NULL,
        date_add TEXT NOT NULL,
        date_remove TEXT,
        condition TEXT CHECK(condition IN ('new', 'old')) NOT NULL,
        status TEXT CHECK(status IN ('owned', 'sold')) NOT NULL,
        resell_value REAL
    )
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS contracts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contract_name TEXT NOT NULL,
        equipment_ids TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        charges REAL NOT NULL
    )''')

conn.commit()
conn.close()