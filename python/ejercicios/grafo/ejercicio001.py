#1. Generar un grafo con 15 vértices aleatorios no repetidos (con números de 1 a 100), luego agregar
#30 aristas –no repetidas– que conecten vértices de manera aleatoria, con etiquetas –también
#aleatorias– dentro del rango de 1 a 100, después resolver las siguientes actividades:

#   a. primero eliminar los vértices que hayan quedado desconectados, es decir, que ningún otro
#       vértice tenga una arista que lo apunte y que de él no salga ninguna arista;
#   b. determinar el nodo con mayor cantidad de aristas que salen de él, puede ser más de uno;
#   c. determinar el nodo con mayor cantidad de aristas que llegan a él, puede ser más de uno;
#   d. indicar los vértices desde los cuales no se puede acceder a otro vértice;
#   e. contar cuantos vértice componen el grafo, dado que se genera aleatoriamente y se eliminan
#       los vértices que quedan desconectados;
#   f. determinar cuántos vértices tienen un arista a sí mismo, es decir, un ciclo directo;
#   g. determinar la arista más larga, indicando su origen, destino y valor –puede ser más de una.

from grafo import Grafo
from grafo import Arista
from random import randint

grafoaleatorio= Grafo(dirigido=False)

for i in range(1,15):
    num = randint(1,100)
    if grafoaleatorio.search_vertice(num) != None:
        grafoaleatorio.insert_vertice(num)
    
for i in range(1,30):
    num1 = randint(1,100)
    num2 = randint(1,100)
    numc = randint(1,100)
    grafoaleatorio.insert_arist(Arista(num2, numc), num1, num2, criterio_arista='vertice')
    
grafoaleatorio.barrido()