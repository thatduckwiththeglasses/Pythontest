#1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.

from Lista import Lista

lista1 = Lista()

lista1.insert(5)
lista1.insert(1)
lista1.insert(8)
lista1.insert(9)
lista1.insert(4)
lista1.insert(10)

cant = lista1.size()

print(f'La cantidad de nodos de esta lista es: {cant}')
