nombre_curso = 'Ultimate Python'
descripcion_curso = '''
Ultimate Python, curso para 
aprender todo lo que se necesita 
para python
'''
print(len(nombre_curso))  # longitud del string
print(nombre_curso[0])  # acceder al primer elemento del string
# acceder al ultimo elemento del string
print(nombre_curso[len(nombre_curso)-1])
# hacer un substring que vaya desde la posicion 0 al 8
print(nombre_curso[0:8])
# hacer un substring que vaya desde la posicion 9 hasta el final del string
print(nombre_curso[9:])
# hacer un substring que vaya desde el inicio del string hasta la posicion 8
print(nombre_curso[:8])
print(nombre_curso[:])  # imprimir todo el string de inicio a fin
