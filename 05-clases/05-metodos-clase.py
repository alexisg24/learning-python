class Perro:
    patas = 4

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")
# Podemos fabricar las clases desde estos metodos, es llamado Factory method

    @classmethod
    def factory(cls):
        # cls o Perro es lo mismo
        return cls("Chanchito feliz", 4)


# cls hace referencia a la clase no a su objeto interno
perro = Perro.factory()
print(perro.edad)
