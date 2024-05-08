if __name__ != "__main__":
    from ..gestion.crud import guardar
    # from usuarios.gestion.crud import guardar

    print(__name__)

    def pagar_impuesto():
        guardar()
        print("Pagar impuesto...")

if __name__ == "__main__":
    print("Tarea de mantenimiento")
