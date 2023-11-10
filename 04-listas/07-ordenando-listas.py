numeros = [2, 6, 89, 8, 1, 96, 5, 43, 35]

# Ordenar de menor a mayor
# numeros.sort()
# Ordenar en reversa
# numeros.sort(reverse=True)

# Devuelve una nueva lista, es decir que no muta
numeros2 = sorted(numeros, reverse=True)

print(numeros2)

usuarios = [['Chanchito', 4], ['Felipe', 1], ['Pulga', 5]]

# Manera clasica de mandar una funcion como parametro
# def ordena(element):
#     return element[1]


# usuarios.sort(key=ordena, reverse=True)

# Usando una funcion anonima o lambda
# usuarios.sort(key=lambda parametros:valorRetorno,reverse=True)
usuarios.sort(key=lambda element: element[1])

print(usuarios)
