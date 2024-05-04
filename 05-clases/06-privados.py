class Perro:
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.__nombre} Guau!")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

# Podemos fabricar las clases desde estos metodos, es llamado Factory method
    @classmethod
    def factory(cls):
        # cls o Perro es lo mismo
        return cls("Chanchito feliz", 4)


# cls hace referencia a la clase no a su objeto interno
perro1 = Perro.factory()

# Acceder a propiedes privadas a traves de un diccionario
# Dict nos da las vairables como _Clase__variable
print(perro1.__dict__["_Perro__nombre"])
