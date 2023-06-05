#7. Eliminar el i-ésimo elemento después del frente de la cola.

from Cola import Cola
from random import randint

cola = Cola()

for i in range(10):
    valor = randint(1,100)
    print(f'Valor agregado: {valor}')
    cola.arrive(valor)

buscado = int(input('Ingrese la posicion del elemento que quiere eliminar: '))

i = 1

total = cola.size()

while total >= i:
    valor = cola.atention()
    if i != buscado:
        cola.arrive(valor)
    i += 1

i = 0

while total >= i:
    valor = cola.atention()
    if valor != None:
        print(valor)
    i += 1