### This is the python file I use to work with the sqlite3 database, since sqlite3 is integrated with python

import sqlite3

conn = sqlite3.connect('items.db')
c = conn.cursor()

# Create items table
c.execute("""CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT
)""")

# Insert some data into the table
items_list = [('jacket', 'fashion'), ('book', 'school supplies'), ('hat', 'fashion')]
c.executemany('INSERT INTO items (name, category) VALUES (?, ?)', items_list)

# Add image column to the table
c.execute("""ALTER TABLE items 
    ADD image TEXT
""")

conn.commit()
conn.close()