import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)'
#
# cursor.execute(create_table)
#
# cursor.execute('INSERT INTO users VALUES (NULL, "kast", "hello")')

result = cursor.execute('SELECT * FROM folders')
print(result.fetchall())

connection.commit()
connection.close()
