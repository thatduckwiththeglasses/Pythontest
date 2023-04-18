#2. Utilizando operaciones de cola y pila, invertir el contenido de una cola.

from Cola import Cola
from Pila import Pila
from random import randint

cola = Cola()
stack = Pila()

for i in range(10):
    valor = chr(randint(65,90))
    print('Valor agregado: ',valor)
    cola.arrive(valor)
    
print(cola.on_front())

while cola.size() > 0:
    stack.apilar(cola.atention())

while stack.size() > 0:
    cola.arrive(stack.desapilar())
    
while cola.size() > 0:
    print(cola.atention())