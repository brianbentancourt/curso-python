import sqlite3

# si utilizamos with no es necesario con.commit() y con.close() ya que internamente se ejecutan desde __exit__
with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )
