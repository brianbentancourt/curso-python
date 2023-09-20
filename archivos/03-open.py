from io import open

# ESCRITURA
# texto = "Hola mundo!"

# archivo = open("archivos/archivo-prueba.txt", "w")
# archivo.write(texto)
# archivo.close()


# LECTURA
# archivo = open("archivos/archivo-prueba.txt", "r")
# texto = archivo.read()
# archivo.close()

# print(texto)

# LECTURA COMO LISTA
# archivo = open("archivos/archivo-prueba.txt", "r")
# texto = archivo.readlines()
# archivo.close()

# print(texto)

# WITH Y SEEK
# Si trabajamos con with, no hay que estar pendiente de tener que cerrar el archivo
# with open("archivos/archivo-prueba.txt", "r") as archivo:
#     # la siguiente instruccion carga todo el arhivo en memoria
#     print(archivo.readlines())

#     # vuelvo el puntero al inicio del archivo nuevamente
#     archivo.seek()

#     # la siguiente linea va cargando el archivo linea a linea
#     for linea in archivo:
#         print(linea)

# AGREGAR
# archivo = open("archivos/archivo-prueba.txt", "a+")
# archivo.write("Bye!")
# archivo.close()

# LECTURA Y ESCRITURA
with open("archivos/archivo-prueba.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "chanchito feliz"
    # me va a reemplazar la cantidad de caracteres
    archivo.writelines(texto)
