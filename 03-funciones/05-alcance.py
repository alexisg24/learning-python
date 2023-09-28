saludo = 'Hola global'


def saludar():
    global saludo
    saludo = 'Hola mundo'
    return saludo


def saludaChanchito():
    saludo = 'Hola Chanchito'
    return saludo
