#5. Utilizando operaciones de cola y pila, invertir el contenido de una pila.

from Cola import Cola
from Pila import Pila
from random import randint

cola = Cola()
stack = Pila()

for i in range(10):
    valor = randint(1,100)
    print(f'Valor agregado: {valor}')
    stack.apilar(valor)
    
while stack.size() > 0:
    cola.arrive(stack.desapilar())

while cola.size() > 0:
    stack.apilar(cola.atention())

while stack.size() > 0:
    print(stack.desapilar())