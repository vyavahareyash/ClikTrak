import sqlite3
from datetime import datetime
import pandas as pd

# Function to insert data into the database
def add_equipment(device_name, nickname, cost, date_add, condition, status="owned"):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO equipment (
            device_name,
            nickname,
            cost,
            date_add,
            condition,
            status
        ) VALUES (?, ?, ?, ?, ?, ?)''',
        (device_name, nickname, cost, date_add, condition, status)
    )
    conn.commit()
    conn.close()
    
def get_owned_equipment():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT device_name, nickname, cost, date_add FROM equipment WHERE status = 'owned'",)
    rows = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(rows, columns=["Device Name", "Nickname", "Cost (INR)", "Date addition"])
    return df