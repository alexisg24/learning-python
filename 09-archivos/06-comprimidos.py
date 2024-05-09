from pathlib import Path
from zipfile import ZipFile

# with ZipFile("09-archivos/comprimidos.zip", "w") as zip:
#     for path in Path().rglob("*.*"):
#         print(path)
#         if str(path) != "09-archivos/comprimidos.zip":
#             zip.write(path)


# with ZipFile("09-archivos/comprimidos.zip", "r") as zip:
#     print(zip.namelist())
#     info = zip.getinfo()
