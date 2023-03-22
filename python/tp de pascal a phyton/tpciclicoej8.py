#8. Se efectúa una encuesta entre 1200 usuarios de sistemas operativos. Las respuestas están
#codificadas como 1, 2 ó 3 según sea el elegido. Preparar un algoritmo para ingresarle las 120
#respuestas, y muestre por pantalla el número del sistema preferido.

from random import randint


cont1 = 0
cont2 = 0
cont3 = 0
i = 0
while i <= 1200:
    so = randint(1,3)
    match so:
        case 1:
            cont1 += 1
        case 2:
            cont2 += 1
        case 3:
            cont3 += 1
    i += 1
if cont1 > cont2 and cont1 > cont3:
    print(f'El sistema operativo mas votado fue el 1 con: {cont1} votos')
elif cont2 > cont3:
    print(f'El sistema operativo mas votado fue el 2 con: {cont2} votos')
else:
    print(f'El sistema operativo mas votado fue el 3 con: {cont3} votos')