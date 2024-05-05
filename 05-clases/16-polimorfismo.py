class Usuario():
    def guardar(self):
        print("Guardando en bdd")


class Session():
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Session()
guardar([usuario, sesion])
