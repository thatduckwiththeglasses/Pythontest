#4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.

from Cola import Cola
from Pila import Pila
from random import randint

cola = Cola()

def numeroprimo(numero):
    contador = 0
    for i in range(2, numero):
        if numero % i == 0:
            contador += 1
            return contador == 0
    return contador == 0

for i in range(10):
    valor = randint(0, 100)
    print('Valor agregado: ',valor)
    cola.arrive(randint(0, 100))
    
contador = 0
cant_elem = cola.size()

while contador < cant_elem:
    if numeroprimo(cola.on_front()):
        cola.atention()
    else:
        cola.motoend()
    contador += 1
    
while cola.size() > 0:
    print(cola.atention())