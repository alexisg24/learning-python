import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lista)

print(
    random.random(),
    random.randint(0, 10),
    list,
    random.choice(lista2),
    random.choices(lista2, k=3),
    "".join(random.choices("ASBDIHdsjfnbsf2131..", k=16)),
)

chars = string.ascii_letters
digitos = string.digits
symbolos = string.punctuation
selection = random.choices(chars+digitos+symbolos, k=16)
print("".join(selection))
