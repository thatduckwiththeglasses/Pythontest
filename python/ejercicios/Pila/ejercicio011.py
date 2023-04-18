#11. Dada una pila de letras determinar cuántas vocales contiene.

from Pila import Pila
from random import randint

stack = Pila()

for i in range(10):
    valor = chr(randint(65,90))
    print(f'Valor agregado: {valor}')
    stack.apilar(valor)

contador = 0

while stack.size() > 0:
    if stack.desapilar() in ['A','E','I','O','U']:
        contador += 1
        
print(f'esta pila contiene {contador} vocales')