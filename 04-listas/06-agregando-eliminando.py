mascotas = ['Pelusa', 'Pulga', 'Felipe',
            'Chanchito Feliz', 'Felipe', 'Wolfgang']

# insertar elementos
mascotas.insert(1, 'Melvin')
mascotas.append('Chanchito Triste')

# Eliminar elementos
# Solo elimina la primera coindicencia
mascotas.remove('Felipe')

# Elimina el ultimo elemento de la lista o el indice que se le indica
mascotas.pop()
mascotas.pop(1)

# eliminar elemento
del mascotas[0]

# Limpiar el array
mascotas.clear()

print(mascotas)
