# Las tuplas es lo mismo que una lista pero no son mutables.
# Es decir podemos crear nuevas en base a ella pero no cambiar las existentes

numeros = (1, 2, 3, 4)
print("numeros", numeros)

# Se pueden concatenar

numeros2 = (1, 2, 3) + (4, 5, 6)
print("numeros2", numeros2)

# Las tuplas se suelen utilizar en elementos que accidentalmente no querramos modificar

# Transformar una lista existente a tupla
# La funcion tuple recibe cualquier elemento que sea iterable
# es decir que tambien funciona con strings

tuplaFromArray = tuple([1, 2])
tuplaFromString = tuple("holas")

# Podemos desestructurarla
one, *rest = tuplaFromArray

# Las tuplas tienen todos los metodos de listas a excepcion de los que la mutan como pop y push
print(tuplaFromArray[:2])
print(tuplaFromString[:2])

# Podemos iterarlas
for char in tuplaFromArray:
    print(char)

# Si queremos alterar algun valor debemos crear una copia de la misma y utilizarla
listFromTuple = list(tuplaFromArray)
listFromTuple[0] = "Chanchito feliz"
print(listFromTuple)
