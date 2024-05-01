# Los diccionarios con un conjunto de datos almacenados por clave-valor

# Las llaves solo se asignan con string mientras el valor puede ser cualquier cosa
# {"clave": valor}
# las claves-valor se separan por comas
punto = {"x": 25, "y": 50}
print(punto)

# Para acceder a algun valor podemos usar el corchete y dentro de el la clave en un string
# parecido a un objeto de js
print(punto["x"])
print(punto["y"])

# Tambien podemos agregar mas llaves a los diccionarios
punto["z"] = 45
print(punto["z"])

# Si queremos acceder a una llave que el valor no existe se lanzara un error
# Podemos manejar esto de 2 maneras, la primera preguntando si existe dentro del diccionario
if "lala" in punto:
    print("lala", punto["lala"])

# Otra opcion es emplear el metodo get que tienen los diccionarios
# Si no existe devolvera un None
print(punto.get("lala"))

# Pero podemos asignarle un valor por defecto en esta misma funcion
print(punto.get("lala", "Default value"))

# Si quiero eliminar alguna clave-valor podemos usar
del punto["x"]

print(punto)

# Pero tambien podemos usar una funcion llamada del
del (punto['y'])
print(punto)

punto['x'] = 25

# Si queremos iterar las llaves con su valor podemos hacer

# Retorna las llaves, Hace lo equivalente a un object.keys
# Para acceder al valor podemnos hacer diccionario[valor]
for valor in punto:
    print(valor, punto[valor])

# Tambien existe otra sintaxis mas facil de obtener los valores
# Donde nos devuelve una tupla donde el primer elemento es la llave y el sedungo es el valor
for valor in punto.items():
    print(valor)

# Pudiendo desestructurarlas asi
for key, valor in punto.items():
    print(valor)


usuarios = [
    {"id": 1, "name": "Canchito"},
    {"id": 2, "name": "Feliz"},
    {"id": 3, "name": "Nicolas"},
    {"id": 4, "name": "Felipe"},
]


for usuario in usuarios:
    print(usuario["name"])
