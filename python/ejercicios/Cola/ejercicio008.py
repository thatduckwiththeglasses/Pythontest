#8. Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando
#   solo una cola como estructura auxiliar.

from Cola import Cola
from random import randint

cola = Cola()
aux = Cola()

for i in range(10):
    valor = randint(1,100)
    print(f'Valor agregado: {valor}')
    cola.arrive(valor)

i = 0

total = cola.size()

while total > 0:
    i = 0
    min = cola.atention()
    max = cola.atention()
    while cola.size() > i:
        valor = cola.atention()
        if max < min:
            cola.arrive(min)
            min = max
            max = valor
        elif min > valor:
            cola.arrive(min)
            min = valor
        elif max < valor:
            cola.arrive(max)
            max = valor
        else:
            cola.arrive(valor)
        i += 1
    aux.arrive(min)
    cola.arrive(max)
    total -= 1
    
while aux.size() > 0:
    cola.arrive(aux.atention())
    
while cola.size() >= 0:
    valor = cola.atention()
    if valor != None:
        print(valor)