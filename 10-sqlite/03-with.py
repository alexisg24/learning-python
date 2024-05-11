import sqlite3

with sqlite3.connect("10-sqlite/app.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios
        (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50));
        """
    )
