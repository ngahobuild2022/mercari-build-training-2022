import sqlite3

# Get all items
def get_all_items():
	conn = sqlite3.connect('..\\db\\items.db')
	c = conn.cursor()

	c.execute("""SELECT items.id, items.name, categories.name, items.image
		FROM items INNER JOIN categories
		ON items.category_id = categories.id
	""")

	fetched_items = c.fetchall()
	items = []

	for item in fetched_items:
		items.append({'id': item[0], 'name': item[1], 'category': item[2], 'image': item[3]})

	conn.close()

	return items

# Insert one item
def insert_item(name, category_id, image):
	conn = sqlite3.connect('..\\db\\items.db')
	c = conn.cursor()

	c.execute('INSERT INTO items (name, category_id, image) VALUES (?, ?, ?)', (name, category_id, image))

	conn.commit()
	conn.close()

	return {'message': f'item received: {name}'}

# Search for items by a keyword
def search_item(keyword):
	conn = sqlite3.connect('..\\db\\items.db')
	c = conn.cursor()

	c.execute(f"""SELECT items.id, items.name, categories.name, items.image
		FROM items INNER JOIN categories
		ON items.category_id = categories.id 
		WHERE items.name LIKE '%{keyword}%'
	""")
	fetched_items = c.fetchall()
	items = []

	for item in fetched_items:
		items.append({'id': item[0], 'name': item[1], 'category': item[2], 'image': item[3]})

	conn.close()

	return items

# Get an item by id
def get_item(id):
	conn = sqlite3.connect('..\\db\\items.db')
	c = conn.cursor()

	c.execute(f"""SELECT items.id, items.name, categories.name, items.image
		FROM items INNER JOIN categories
		ON items.category_id = categories.id 
		WHERE items.id={id}
	""")
	item = c.fetchone()

	conn.close()

	return {'id': item[0], 'name': item[1], 'category': item[2], 'image': item[3]}