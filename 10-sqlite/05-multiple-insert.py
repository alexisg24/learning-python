import sqlite3

with sqlite3.connect("10-sqlite/app.db") as connection:
    cursor = connection.cursor()
    usuarios = [
        (2, "Chamchito feliz"),
        (3, "Chamchito triste"),
    ]
    cursor.executemany(
        """
        INSERT INTO usuarios VALUES(?, ?)
        """,
        usuarios
    )
