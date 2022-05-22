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

# Remove the category column & add a new table for categories
c.execute("ALTER TABLE items DROP COLUMN category")
c.execute("""CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)""")
c.execute("ALTER TABLE items ADD COLUMN category_id INTEGER REFERENCES categories(id)")

# Add some data to categories table & update relevant records in items table
categories_list = [('fashion',), ('school supplies',)]
c.executemany('INSERT INTO categories (name) VALUES (?)', categories_list)
linked_items_categories_list = [(1, 1), (2, 2), (1, 3)]
c.executemany('UPDATE items SET category_id=(?) WHERE id=(?)', linked_items_categories_list)

conn.commit()
conn.close()