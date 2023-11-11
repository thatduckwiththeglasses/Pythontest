#14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes
#tareas:
#   a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
#       baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
#   b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
#       es la distancia entre los ambientes, se debe cargar en metros;
#   c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#       para conectar todos los ambientes;
#   d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#       determinar cuántos metros de cable de red se necesitan para conectar el router con el
#       Smart Tv.

from grafo import Grafo
from grafo import Arista
from random import randint

grafocasa = Grafo(dirigido=False)
lista_habitaciones = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2', 'habitación 1', 'habitación 2', 'sala de estar', 'terraza', 'patio']

for habitacion in lista_habitaciones:
    grafocasa.insert_vertice(habitacion)

for habitacion in lista_habitaciones:
    for habitacion2 in lista_habitaciones:
        if habitacion.startswith(habitacion2) == False:
            grafocasa.insert_arist(habitacion,habitacion2,randint(0,10))

min = [99]
bosque = grafocasa.kruskal()
for arbol in bosque:
    for nodo in arbol.split(';'):
        for value in nodo.split('-'):
            if (value[0] in ['0','1','2','3','4','5','6','7','8','9']) and (value[-1] in ['0','1','2','3','4','5','6','7','8','9']):
                if min[0] >= int(value):
                    min.clear()
                    min.append(int(value))
                    min.append(nodo)

print(f'arbol de expansion minima: {min[1]}')

ori = 'habitación 1'
des = 'sala de estar'
origen = grafocasa.search_vertice(ori, criterio='nombre')
destino = grafocasa.search_vertice(des, criterio='nombre')
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(grafocasa.has_path(ori, des, criterio='nombre')):
        camino_mas_corto = grafocasa.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.desapilar()
            if fin == value[0]:
                print(value[0], value[1])
                fin = value[2]
    
