import sqlite3

# si el archivo app.db no existe, python lo crea
con = sqlite3.connect("sqlite/app.db")
# siempre hay que cerrar la conexion
con.close()
