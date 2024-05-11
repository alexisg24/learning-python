import sqlite3

connection = sqlite3.connect("10-sqlite/app.db")
cursor = connection.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios
    (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50));
    """
)
connection.commit()
connection.close()
