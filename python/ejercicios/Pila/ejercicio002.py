#2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden nú-
#   meros pares.

from Pila import Pila
from random import randint

stack = Pila()
stack_aux = Pila()

for i in range(10):
    valor = randint(0,100)
    print('valor agregado', valor)
    stack.apilar(valor)
    
while stack.size() > 0:
    valor = stack.desapilar()
    if valor % 2 == 0:
        stack_aux.apilar(valor)
        
while stack_aux.size() > 0:
    stack.apilar(stack_aux.desapilar())

while stack.size() > 0:
    print(stack.desapilar())