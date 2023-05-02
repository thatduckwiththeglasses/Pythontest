#6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna
#   estructura auxiliar.

from Cola import Cola
from random import randint

cola = Cola()

for i in range(10):
    valor = randint(1,100)
    print(f'Valor agregado: {valor}')
    cola.arrive(valor)

buscado = int(input('Ingrese el elemento que quiere buscar: '))

i = 0
    
contador = 0

while cola.size() > i:
    valor = cola.atention()
    if valor == buscado:
        contador += 1
    cola.arrive(valor)
    i += 1

print(f'El elemento aparece: {contador} veces')