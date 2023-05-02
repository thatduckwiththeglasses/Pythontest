#3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar
#   si es un palíndromo.

from Cola import Cola
from Pila import Pila

palabra = input()

cola = Cola()
pila = Pila()

for letra in palabra:
    cola.arrive(letra)

size = cola.size()
while cola.size() > (size // 2):
    pila.apilar(cola.atention())
        

while cola.size() > 0 and pila.size() > 0:
    if size % 2 == 0:
        if cola.on_front() != pila.ontop():
            print('no es palindromo')
            break
        else:
            cola.atention()
            pila.desapilar()
    else:
        cola.atention()
        if cola.on_front() != pila.ontop():
            print('no es palindromo')
            break
        else:
            cola.atention()
            pila.desapilar()
            
if pila.size() == 0:
    print('es palindromo')
    
