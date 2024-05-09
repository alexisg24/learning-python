import json
from pathlib import Path

# escribir
# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"},
# ]

# data = json.dumps(productos)
# Path("09-archivos/productos.json").write_text(data, encoding="utf-8")

# Leer
data = Path("09-archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)


# modificar json
productos[0]["name"] = "Chanchito feliz"
encoded_data = json.dumps(productos)
Path("09-archivos/productos.json").write_text(encoded_data, encoding="utf-8")
