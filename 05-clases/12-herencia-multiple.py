class Animal:
    def comer(self):
        print("Comiendo")


class Perro:
    def pasear(self):
        print("Paseando")


class Chanchito(Perro, Animal):
    def programar(self):
        print("Programando")


perro = Perro()
chanchito = Chanchito()
chanchito.comer()
