class Perro:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre


perro = Perro("Choclo")
print(perro.nombre)
