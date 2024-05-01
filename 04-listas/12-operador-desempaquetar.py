# si queremos desmpaquetar que es parecido al spread operator
# Sirve con cualquier iterable
lista = [1, 2, 3, 4]
print(1, 2, 3, 4)
print(*lista)


# tambien podemos unir listas
lista2 = [5, 6]

combinada = [*lista, *lista2]
print(combinada)


# Usando diccionarios:
punto1 = {"x": 19, "y": 10}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
