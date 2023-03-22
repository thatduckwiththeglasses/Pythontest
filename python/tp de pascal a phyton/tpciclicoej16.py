#16. Construir un algoritmo que, dada una secuencia de enteros acabada con el valor cero, devuelva el
#mayor de ellos. Determinar cuántos números negativos han aparecido.

from random import randrange

v = []
a = input('Quiere comensar?(S para si, N para no) ')
cont = 0
print(a)
while a.upper() == 'S':
    b = int(input('Ingrese un numero: '))
    if b < 0:
        cont += 1
    v.extend([b])
    a = input('Quiere seguir?(S para si, N para no) ')
v.sort()
print(v[-1], cont)