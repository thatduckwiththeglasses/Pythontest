#9. Desarrollar un algoritmo que determine en un conjunto de 100 números:
#	a) Cuántos son mayores que 15.
#	b) Cuántos son mayores que 50.
#	c) Cuántos están comprendidos entre 25 y 45.
from random import randint

i = 0
cont15 = 0
cont50 = 0
cont25 = 0 
while i <= 100:
    num = randint(1,100)
    if num > 15:
        cont15 += 1
        if num > 25 and num < 45:
            cont25 += 1
        elif num > 50:
            cont50 += 1
    i += 1
print('cantidad de numeros mayores que 15: ',cont15)
print('cantidad de numeros entre 25 y 45: ',cont25)
print('cantidad de numeros mayores que 50: ',cont50)