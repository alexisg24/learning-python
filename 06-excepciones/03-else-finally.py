try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as ex:
    print("Ingrese un valor valido!")
else:  # Se ejecuta siempre que no hay errores
    print("No ocurrio ningun error")
finally:  # Se ejecuta siempre al final dfel try/catch
    print("Se finalizo la ejecucion")
