#2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
#algoritmos necesarios para resolver las siguientes tareas:
#   a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
#       cantidad de episodios en los que aparecieron juntos ambos personajes que se
#       relacionan;
#   b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
#   c) determinar cuál es el número máximo de episodio que comparten dos personajes,
#       y quienes son.
#   d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda,
#       Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.

from grafo import Grafo
from grafo import Arista
from random import randint

grafosw= Grafo(dirigido=False)

grafosw.insert_vertice('Luke Skywalker')
grafosw.insert_vertice('Darth Vader')
grafosw.insert_vertice('Yoda')
grafosw.insert_vertice('Boba Fett')
grafosw.insert_vertice('C-3PO')
grafosw.insert_vertice('Leia')
grafosw.insert_vertice('Rey')
grafosw.insert_vertice('Kylo Ren')
grafosw.insert_vertice('Chewbacca')
grafosw.insert_vertice('Han Solo')
grafosw.insert_vertice('R2-D2')
grafosw.insert_vertice('BB-8')

grafosw.insert_arist(Arista('Luke Skywalker',12), 'Boba Fett', 'Luke Skywalker', criterio_arista='arista')
grafosw.insert_arist(Arista('Luke Skywalker',20), 'Yoda', 'Luke Skywalker', criterio_arista='arista')
grafosw.insert_arist(Arista('R2-D2',12), 'Boba Fett', 'R2-D2', criterio_arista='arista')
grafosw.insert_arist(Arista('R2-D2',12), 'Luke Skywalker', 'R2-D2', criterio_arista='arista')
grafosw.insert_arist(Arista('Leia',10), 'Yoda', 'Leia', criterio_arista='arista')
grafosw.insert_arist(Arista('R2-D2',14), 'Leia', 'R2-D2', criterio_arista='arista')

max = [0]
min = [99]
bosque = grafosw.kruskal()
for arbol in bosque:
    for nodo in arbol.split(';'):
        if (nodo != 'BB-8'):
            for value in nodo.split('-'):
                if (value[0] in ['0','1','2','3','4','5','6','7','8','9']) and (value[-1] in ['0','1','2','3','4','5','6','7','8','9']):
                    if max[0] <= int(value):
                        max.clear()
                        max.append(int(value))
                        max.append(nodo)
                    if min[0] >= int(value):
                        min.clear()
                        min.append(int(value))
                        min.append(nodo)

for value in min[1].split('-'):
    if value == 'Yoda':
        print('si contiene a Yoda')
print(f'Arbol de expansion minimo: {min.pop()}')

print(f'Personajes que mas comparten episodios: {max.pop()}')

print(bosque)