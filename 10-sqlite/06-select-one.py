import sqlite3

with sqlite3.connect("10-sqlite/app.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchone())
