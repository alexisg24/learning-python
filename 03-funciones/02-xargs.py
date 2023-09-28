def suma(*numeros):
    res = 0
    for numero in numeros:
        res += numero
    print(res)


suma(2, 5)
suma(2, 5, 3)
