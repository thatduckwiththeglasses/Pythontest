#9. Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.

from Cola import Cola
from random import randint

cola = Cola()

for i in range(10):
    valor = randint(-100,100)
    print(f'Valor agregado: {valor}')
    cola.arrive(valor)
    
total = cola.size()

i = 0

contador = 0

while total > i:
    valor = cola.atention()
    if valor < 0:
        contador += 1
    i += 1

i = 0

while cola.size() >= i:
    valor = cola.atention()
    if valor != None:
        print(valor)
    i += 1

print(f'Cantidad de valores negativos: {contador}')