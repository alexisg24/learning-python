from pathlib import Path

archivo = Path("09-archivos/archivo-prueba.txt")
texto = archivo.read_text(encoding="utf-8").split("\n")
texto.insert(0, "Hola mundo!")
archivo.write_text("\n".join(texto), "utf-8")
print(texto)
