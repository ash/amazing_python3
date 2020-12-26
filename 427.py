# Using "Unix DBs"

import dbm

with dbm.open('db.db', 'c') as db:
    # 'db.db' - filename
    # 'c' - open for write/read; create
    db["key1"] = 'Value A'
    db["key2"] = 'Value B'

# .... some other part of the program
# or another program .....
with dbm.open('db.db', 'c') as db:
    print(db["key1"])
    print(db["key2"])
