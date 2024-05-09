import csv
import os
from io import open


# escribir
with open("09-archivos/archivo.csv", "w", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["twit_id", "user_id", "text"])
    writer.writerow([100, 1, "este es un tweet"])
    writer.writerow([1001, 2, "este es otro tweet"])


# leer
# with open("09-archivos/archivo.csv", encoding="utf-8") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for line in reader:
#         print(line)


# actualizar CSV
with open("09-archivos/archivo.csv", "r", encoding="utf-8") as r, open("09-archivos/archivo_temp.csv", "w", encoding="utf-8") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)

    for line in reader:
        if len(line) > 0:
            if line[0] == "100":
                writer.writerow([100, 1, "nuevo tweeet"])
            else:
                writer.writerow(line)
    r.close()
    w.close()
    os.remove("09-archivos/archivo.csv")
    os.rename("09-archivos/archivo_temp.csv", "09-archivos/archivo.csv")
