from pathlib import Path
from zipfile import ZipFile

# ESCRIBIR
# with ZipFile("archivos/comprimido.zip", "w") as zip:
#     for path in Path().rglob("*.*"):
#         if str(path) != "archivos/comprimidos.zip":
#             if not any(part.startswith('.') for part in path.parts):
#                 zip.write(path)

# LEER
with ZipFile("archivos/comprimidos.zip") as zip:
    # print(zip.namelist())
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size
    )
    zip.extractall("archivos/descomprimidos")
