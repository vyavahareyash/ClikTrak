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
    
def add_contract(contract_name, equipment_ids, start_date, end_date, charges):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO contracts (
        contract_name, equipment_ids, start_date, end_date, charges
    ) VALUES (?, ?, ?, ?, ?)''', (contract_name, equipment_ids, start_date, end_date, charges))
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

def get_equip():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, device_name FROM equipment WHERE status = 'owned'")
    owned_equipment = cursor.fetchall()
    conn.close()
    equips = {str(equip[0]): equip[1] for equip in owned_equipment}
    
    return equips

def get_contracts():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT contract_name, equipment_ids, start_date, end_date, charges FROM contracts",)
    rows = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(rows, columns=["Contract Name", "Equips", "Start Date", "End Date", "Charges"])
    return df