from pathlib import Path

Path(r"E:\Dev\Ultimate Python")  # Windows
Path(r"/usr/bin")  # Linux/Mac OS
Path()  # Path root de la app
Path().home()  # Path home del usuario
Path("one/__init__.py")  # Ruta relativa del proyecto actual

path = Path("hola-mundo/mi-archivo.py")  # Este path puede o no existir
path.is_file()  # Revisa si es archivo
path.is_dir()  # Revisa si es un directorio
path.exists()  # Revisa si existe

print(
    path.name,  # Nombre del archivo con extension
    path.stem,  # Nombre del archivo sin extension
    path.suffix,  # Extension del archivo
    path.parent,  # Directorio padre de donde se encuentra el path
    path.absolute()  # Ruta absoluta del archivo
)

# Nos permite cambiar el nombre del archivo con extension
p = path.with_name("chanchito.py")
p = path.with_suffix(".bat")  # Nos permite cambiar la extension del archivo
p = path.with_stem("feliz")  # Nos permite cambiar el nombre del archivo

print(p)
