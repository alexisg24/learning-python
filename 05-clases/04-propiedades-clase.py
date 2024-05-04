class Perro:
    patas = 4

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Chanchito", 1)
mi_perro.habla()
print(Perro.patas)
