from io import open

# escritura
# texto = "Hola mundo"
# archivo = open("09-archivos/archivo-prueba.txt", "w", encoding="utf-8")
# archivo.write(texto)
# archivo.close()

# lectura
# archivo = open("09-archivos/archivo-prueba.txt", "r", encoding="utf-8")
# texto = archivo.read()
# archivo.close()
# print(texto)


# lectura como lista
# archivo = open("09-archivos/archivo-prueba.txt", "r", encoding="utf-8")
# texto = archivo.readlines()
# archivo.close()
# print(texto)


# with cierra los archvios automaticamente y si hay un error lanzara una exception
# with open("09-archivos/archivo-prueba.txt", "r", encoding="utf-8") as archivo:
# carga todo el archivo en memoria pero una vez rcorrido no ejecuta el for
# print(archivo.readlines())
# archivo.seek(0)  # volver al caracter 0
# for line in archivo:  # carga 1 linea a la vez
#     print(line)


# agregar
# archivo = open("09-archivos/archivo-prueba.txt", "a+", encoding="utf-8")
# archivo.write("Chao mundo!")
# archivo.close()

# Lectura y escritura r+
with open("09-archivos/archivo-prueba.txt", "r+", encoding="utf-8") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)  # movemos el puntero al valor 0
    texto[0] = "Chanchito feliz"
    archivo.writelines(texto)
