import sqlite3

def createTable():
    conn = sqlite3.connect('laundry.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS cucian (nama TEXT, jumlah INTEGER)")
    conn.commit()
    conn.close()

def insert():
    conn = sqlite3.connect('laundry.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO cucian VALUES ('Dika', 29)")
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('laundry.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM cucian")
    rows = cur.fetchall()
    conn.close()
    return rows

createTable()
# insert()

print(view())
