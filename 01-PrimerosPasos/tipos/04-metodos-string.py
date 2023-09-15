animal = '  chanchito feliz '
print(animal.upper()) #mayusculas
print(animal.lower()) #minusculas
print(animal.capitalize()) #Primera letra mayus
print(animal.title()) #Cada inicio de palabra en mayus
print(animal.strip()) #quitar espacios al inicio y final
print(animal.rstrip()) #Quitar espacios a la derecha
print(animal.lstrip()) #Quitar espacios a la izquierda
print(animal.find('ch')) #Retornar indice si lo encuentra
print(animal.replace('nch', 'j')) #Reemplaza una cadena por otra
print('nch' in animal) #Retorna un boolean si existe o no esta cadena en la variable
print('nch' not in animal) #Retorna un boolean negado si existe o no esta cadena en la variable
