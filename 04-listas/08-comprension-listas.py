usuarios = [['Chanchito', 4], ['Felipe', 1], ['Pulga', 5]]

# Obtener solo el listado de nombres de este arreglo, parecido a la funcion Map de js

# Forma clasica con for
nombres = []

for nombre, *_ in usuarios:
    nombres.append(nombre)

print(nombres)


# Forma de hacerla con un metodo propio como el map
# map = [expression for item in items]
# Donde items hace referencia al arreglo
# Item es el nombre elemento de la lista que estamos iterando
# Y la expresion es la transformacion que le aplicaremos al elemento

# map
userNames = [usuario[0] for usuario in usuarios]
print('userNames', userNames)


# Para filtarlos podemos emplear una manera similar que actua como el metodo filter de js
# filteredNames = [expression for item in items if condicion]
# Ahora el metodo lleva una condicion
# Y retorna la expresion si cumple con la condicion

# filter
filteredNames = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print('filteredNames', filteredNames)


names = list(map(lambda usuario: usuario[0], usuarios))
print('names', names)


lessNames = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print('lessNames', lessNames)
