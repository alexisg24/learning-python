numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, *otros, penultimo, ultimo = numeros
print(primero, penultimo, ultimo, otros)
