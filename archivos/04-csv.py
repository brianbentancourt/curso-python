import csv
import os

# ESCRIBIR
# with open("archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow(["100", "1", "este es un twit"])
#     writer.writerow(["102", "2", "otro twit"])

# LEER
# with open("archivos/archivo.csv", "r") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# ACTUALIZAR CSV
with open("archivos/archivo.csv", "r") as r, open("archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "100":
            writer.writerow([100, 1, "texto modificado"])
        else:
            writer.writerow(linea)
    os.remove("archivos/archivo.csv")
    os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
