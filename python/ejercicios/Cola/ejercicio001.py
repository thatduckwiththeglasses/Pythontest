#1. Eliminar de una cola de caracteres todas las vocales que aparecen.

from Cola import Cola
from random import randint

cola = Cola()

for i in range(10):
    valor = chr(randint(65,90))
    print('Valor agregado: ',valor)
    cola.arrive(valor)

j = 0
    
while j < cola.size():
    if cola.on_front() in ['a','e','i','o','u','A','E','I','O','U']:
        cola.atention()
    else:
        cola.motoend()
    j += 1
        
while cola.size() > 0:
    print(cola.atention())
    
