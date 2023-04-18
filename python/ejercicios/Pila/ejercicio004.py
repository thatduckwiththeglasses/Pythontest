#4. Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

from Pila import Pila
from random import randint

pila = Pila()
lista = []

for i in range(10):
    valor = randint(0,100)
    print('valor agregado', valor)
    pila.apilar(valor)

j = 0

while pila.size() < j:
    lista[j] = pila.desapilar()
    j += 1

while len(lista) > 0:
    pila.apilar(lista.pop(-1))
    
while pila.size() > 0:
    print(pila.desapilar())