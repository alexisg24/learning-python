buscar = 20

# for numero in range(5):
#     print(numero, numero * 'hola mundo')

for numero in range(5):
    print(numero)
    if numero == buscar:
        print('encontrado', buscar)
        break
else:
    print('no encontrado')


for char in "ultimate python":
    print(char)
