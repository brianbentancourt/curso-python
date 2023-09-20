import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Chanchito feliz"),
        (3, "Chanchito triste")
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios,
    )
