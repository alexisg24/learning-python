'''
Ejercicio
'''

NUMERO_1 = False
NUMERO_2 = False

print('Bienvenido a la calculadora')
while True:
    if not NUMERO_1:
        NUMERO_1 = float(input('Ingrese primer numero: '))
    else:
        operador = input('Ingrese una operacion (suma, resta, mul, div): ')
        NUMERO_2 = float(input('Ingrese segundo numero: '))

        if operador == 'suma':
            NUMERO_1 += + NUMERO_2
            print('El resultado es: ', NUMERO_1)
        elif operador == 'resta':
            NUMERO_1 -= + NUMERO_2
            print('El resultado es: ', NUMERO_1)
        elif operador == 'mul':
            NUMERO_1 *= + NUMERO_2
            print('El resultado es: ', NUMERO_1)
        elif operador == 'div':
            NUMERO_1 /= + NUMERO_2
            print('El resultado es: ', NUMERO_1)
        else:
            print('No se selecciono un operador valido.')
            break
