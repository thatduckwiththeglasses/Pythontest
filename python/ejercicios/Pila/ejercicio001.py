#1. Determinar el número de ocurrencias de un determinado elemento en una pila.

from Pila import Pila
from random import randint

pila = Pila()

for i in range(10):
    valor = randint(0,100)
    print('valor agregado', valor)
    pila.apilar(valor)
    
buscado = int(input())
contador = 0

while pila.size() > 0:
    if pila.desapilar() == buscado:
        contador += 1

print(f'El elemento {buscado} aparece {contador} veces en la pila')