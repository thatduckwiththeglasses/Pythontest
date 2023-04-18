#3. Reemplazar todas las ocurrencias de un determinado elemento en una pila

from Pila import Pila
from random import randint

pila = Pila()
pila_aux = Pila()

for i in range(10):
    valor = randint(0,100)
    print('valor agregado', valor)
    pila.apilar(valor)
    
buscado = int(input())

while pila.size() > 0:
    num = pila.desapilar()
    if num != buscado:
        pila_aux.apilar(num)

while pila_aux.size() > 0:
    pila.apilar(pila_aux.desapilar())
    
while pila.size() > 0:
    print(pila.desapilar())

