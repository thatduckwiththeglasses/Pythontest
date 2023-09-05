#2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

from Lista import Lista
from random import randint

letras = Lista()

for i in range(100):
    valor = chr(randint(65,90))
    print('Valor agregado: ',valor)
    letras.insert(valor)
    
vocales = ['A','E','I','O','U','a','e','i','o','u']

index = 0
while index < letras.size():
    valor = letras.get_element_by_index(index)
    if valor in vocales:
        letras.delete(valor)

letras.barrido()