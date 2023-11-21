#A continuación se plantean una serie de problemas, que se deberán resolver utilizar el TDA árbol
#binario de búsqueda AVL, salvo que el ejercicio pida utilizar otro tipo particular de árbol.
#1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria–
#que resuelva las siguientes actividades:
#a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
#b. determinar si un número está cargado en el árbol o no;
#c. eliminar tres valores del árbol;
#d. determinar la altura del subárbol izquierdo y del subárbol derecho;
#e. determinar la cantidad de ocurrencias de un elemento en el árbol;
#f. contar cuántos números pares e impares hay en el árbol.

from arbol import BinaryTree
from random import randint

arbol = BinaryTree()

for i in range(30):
    arbol.insert_node(randint(0, 30))

#! A falta por nivel
print('inorden')
arbol.inorden()
# print()
# print('postorden')
# arbol.postorden()
# print()
# print('preorden')
# arbol.preorden()

#! B
# numero = int(input('ingrese un numero: '))
# pos = arbol.search(numero)
# if pos:
#     print(f'{numero} esta cargado en el arbol')

#! C
for i in range(3):
    numero = int(input('Ingrese un numero para eliminar: '))
    deleted_value = arbol.delete_node(numero)
    if deleted_value:
        print(f'el valor {numero} fue eliminado')
    else:
        print('Este valor no existe')
arbol.inorden()

#! D

numero = int(input('Ingrese un numero para contar: '))
