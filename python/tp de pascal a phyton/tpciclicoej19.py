#19. Contar la cantidad de Números negativos de una lista que finaliza con el No 0.

from random import randint


a = randint(-500,500)
sec = []
cont = 0
while a != 0:
    sec.extend([a])
    if a < 0:
        cont += 1
    a = randint(-500,500)
print(cont)
