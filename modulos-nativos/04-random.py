import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

random.shuffle(lista)

print(
    random.random(),
    random.randint(1, 100),
    lista,
    random.choice(lista2),
    random.choices(lista2, k=3),
    random.choices("sh2fksdh14kas5d", k=3),
)

CHARS = string.ascii_letters
DIGITOS = string.digits
seleccion = random.choices(CHARS + DIGITOS, k=16)

PASSWORD = "".join(seleccion)
print(PASSWORD)
