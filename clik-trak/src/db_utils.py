from tinydb import TinyDB, Query

db = TinyDB("storage/data/contracts_db.json")

contracts_table = db.table("contracts")
tasks_master = db.table("tasks")
tags_master = db.table("tags")

Q = Query()

def get_all_contracts():
    return contracts_table.all()

if __name__ == "__main__":
    print(get_all_contracts())