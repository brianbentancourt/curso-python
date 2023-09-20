import json
from pathlib import Path

# ESCRIBIR JSON
# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bike"},
#     {"id": 3, "name": "Skate"}
# ]

# data = json.dumps(productos)
# Path("archivos/productos.json").write_text(data)

# LEER JSON
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)

# MODIFICAR JSON
productos[0]["name"] = "Chanchito feliz"
Path("archivos/productos.json").write_text(json.dumps(productos))
