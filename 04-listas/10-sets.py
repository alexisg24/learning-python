# Set significa grupo o conjunto
# Un set es una coleccion de datos no ordenada y que no se repiten sus valores

firstSet = {1, 1, 2, 2, 3, 3, 4}
print(firstSet)  # result: {1, 2, 3, 4}

# Los sets se manejan similares a las litas ya que possen metodos parecidos
# Para agregar un elemento usamos
firstSet.add(5)

# Para eliminar un elemento usamos
firstSet.remove(1)

print(firstSet)  # result: {2, 3, 4, 5}


secondSet = [3, 4, 5]

# Para transformar una lista a un set utilizamos la funcion set la cual recibe un iterable
secondSet = set(secondSet)
print(secondSet)

# Lo interesante de los sets es que poseen operadores que permiten unirlos y hacer operaciones
# complejas con ellos

setA = {1, 1, 1, 2, 3, 3, 4}
setB = {5, 5, 5, 1, 2, 5, 6, 6}

# Operador union junta ambos sets
print(setA | setB)  # Res: {1, 2, 3, 4, 5, 6}

# Operador de intersection, solo muestra los elementos que se interceptan
# es decir que ambos tengan en comun
print(setA & setB)  # Res: {1, 2,}

# Operador de diferencias, solo muestra los elementos que se encuentran en el
# conjunto de la izquierda y le quitamos los que tengan en comun con el de la derecha
print(setA - setB)  # Res: {3, 4}


# Operador de diferencia simetrica
# Solo muestra los elementos que no se encuentran en ambos sets
print(setA ^ setB)


# El problema de los sets es que no se pueden ordear ni acceder a un elemento especifico de ellos
# Es por ello que se pueden hacer validaciones con un if par ver si existe el valor. Ejemplo:
if 5 in setB:
    print("Hola!")
