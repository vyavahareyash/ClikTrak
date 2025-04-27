# db.py
from tinydb import TinyDB, Query
import uuid

db = TinyDB("contracts_db.json")

contracts_table = db.table("contracts")
tasks_master = db.table("tasks")
tags_master = db.table("tags")

Q = Query()

def add_task(task_name: str):
    if not tasks_master.get(Q.name == task_name):
        tasks_master.insert({"type": task_name})
        
def get_tasks():
    tasks = tasks_master.all()
    return [task["type"] for task in tasks]

def add_tag(tag_name: str):
    if not tags_master.get(Q.name == tag_name):
        tags_master.insert({"name": tag_name})

def delete_tag(tag_name: str):
    tag = tags_master.get(Q.name == tag_name)
    if tag:
        tags_master.remove(Q.name == tag_name)
        return True
    else:
        return False

def get_tags():
    tags = tags_master.all()
    return [tag["name"] for tag in tags]

def add_contract(contract_data):
    contract_id = str(uuid.uuid4())
    contract_data["id"] = contract_id
    contracts_table.insert(contract_data)
    return

def get_all_contracts():
    return contracts_table.all()

def get_contract(contract_id):
    contract = contracts_table.get(Q.id == contract_id)
    if contract:
        return contract
    else:
        return None

def update_contract(contract_id: str, updated_data: dict):
    contract = contracts_table.get(Q.id == contract_id)
    if contract:
        contracts_table.update(updated_data, Q.id == contract_id)
        return True
    else:
        return False

def delete_contract(contract_id: str):
    contract = contracts_table.get(Q.id == contract_id)
    if contract:
        contracts_table.remove(Q.id == contract_id)
        return True
    else:
        return False
    
def get_contract_id_by_name(contract_name: str):
    contract = contracts_table.get(Q.contract_name == contract_name)
    if contract:
        return contract["id"]
    else:
        return None