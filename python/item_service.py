import sqlite3

# Get all items
def get_all_items():
	conn = sqlite3.connect('..\\db\\items.db')
	c = conn.cursor()

	c.execute('SELECT * FROM items')
	fetched_items = c.fetchall()
	items = []

	for item in fetched_items:
		items.append({'id': item[0], 'name': item[1], 'category': item[2]})

	conn.close()

	return items

# Insert one item
def insert_item(name, category, image):
	conn = sqlite3.connect('..\\db\\items.db')
	c = conn.cursor()

	c.execute('INSERT INTO items (name, category) VALUES (?, ?)', (name, category))

	conn.commit()
	conn.close()

	return {'message': f'item received: {name}'}

# Search for items by a keyword
def search_item(keyword):
	conn = sqlite3.connect('..\\db\\items.db')
	c = conn.cursor()

	c.execute(f"SELECT * FROM items WHERE name LIKE '%{keyword}%'")
	fetched_items = c.fetchall()
	items = []

	for item in fetched_items:
		items.append({'id': item[0], 'name': item[1], 'category': item[2]})

	conn.close()

	return items