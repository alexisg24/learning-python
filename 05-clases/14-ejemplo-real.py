class Model:
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una table")

    def guardar(self):
        print(f"Guardando {self.tabla} en db")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id: {_id} en la tabla ")


class User(Model):
    tabla = "Usuario"


usuario = User()
usuario.guardar()
Model.buscar_por_id(1)
