from pathlib import Path
path = Path("08-rutas")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("chanchito-feliz")

# for p in path.iterdir():
#     print(p)

# archivos = [p for p in path.iterdir() if not p.is_dir()]
# Todos los archivos que tengan extension .py
archivos = [p for p in path.glob("*.py")]

# Todos los archivos que tengan extension .py y comiencen por 01-
archivos2 = [p for p in path.glob("01-*.py")]

# Todos los archivos que tengan extension .py que se encuentgren en todas las carpetas
archivos3 = [p for p in path.glob("**/*.py")]

# Todos los archivos que tengan extension .py que se encuentgren en todas las carpetas de manere recursiva
archivos4 = [p for p in path.rglob("*.py")]

print(archivos)
print(archivos2)
print(archivos3)
print(archivos4)
