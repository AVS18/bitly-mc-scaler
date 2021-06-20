import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
cur.execute('select * from base_url;')
for obj in cur.fetchmany():
    print(obj)