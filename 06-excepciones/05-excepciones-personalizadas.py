class MiError(Exception):
    "Esta clase es para representar mi error"  # </ documentacion

    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"{self.message} - {self.status_code}"


def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir por 0", 404)
    return 5/n


try:
    division()
except MiError as e:
    print(e)
