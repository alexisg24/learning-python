# Pila - Lifo
pila = []
pila.append(1)
pila.append(2)

print(pila)
ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)
print(pila[-1])
pila.pop()


if not pila:
    print("Pila vacia")
