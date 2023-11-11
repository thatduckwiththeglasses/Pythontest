#15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas
#y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
#   a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
#       uno en las naturales) y tipo (natural o arquitectónica);
#   b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
#       la distancia que las separa;
#   c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
#   d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
#   e. determinar si algún país tiene más de una maravilla del mismo tipo;
#   f. deberá utilizar un grafo no dirigido.

from grafo import Grafo
from grafo import Arista
from random import randint

class Maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
    
    def __str__(self):
        return f'{self.nombre} - {self.pais} - {self.tipo}'
        

grafomaravillas = Grafo(dirigido=False)

lista_maravillas = [Maravilla('La Gran Muralla','China','Arquitectonica'),
                    Maravilla('Petra','Jordania','Arquitectonica'),
                    Maravilla('El Coliseo','Italia','Arquitectonica'),
                    Maravilla('Chichen Itza','Mexico','Arquitectonica'),
                    Maravilla('Machu Picchu','Peru','Arquitectonica'),
                    Maravilla('Cristo Redentor','Brasil','Arquitectonica'),
                    Maravilla('Taj Mahal','India','Arquitectonica'),
                    Maravilla('Bahía de Ha Long','Vietnam','Natural'),
                    Maravilla('Isla de Komodo','Indonesia','Natural'),
                    Maravilla('Río subterráneo de Puerto Princesa','Filipinas','Natural'),
                    Maravilla('Montaña de la Mesa','Sudafrica','Natural'),
                    Maravilla('Cataratas del Iguazú','Argentina','Natural'),
                    Maravilla('Río Amazonas','Peru','Natural'),
                    Maravilla('Isla de Jeju','Corea del Sur','Natural')]

for maravilla in lista_maravillas:
    grafomaravillas.insert_vertice(maravilla,criterio='nombre')

for maravilla in lista_maravillas:
    for maravilla2 in lista_maravillas:
        if (maravilla.nombre != maravilla2.nombre) and (maravilla.tipo == maravilla2.tipo):
            valordist = randint(0,10)
            grafomaravillas.insert_arist(maravilla.nombre,maravilla2.nombre,valordist,criterio_vertice='nombre')

minar = 99
minnat = 99
minarbolnat = None
minarbolar = None
distancia = 0

bosque = grafomaravillas.kruskal()
for arbol in bosque:
    for nodo in arbol.split(';'):
        for dato in nodo.split('-'):
            if (dato[0] in ['0','1','2','3','4','5','6','7','8','9']) and (dato[-1] in ['0','1','2','3','4','5','6','7','8','9']):
                distancia = dato
            else:   
                pos = grafomaravillas.search_vertice(dato,criterio='nombre')
                value = grafomaravillas.get_element_by_index(pos)
                if (value[0].tipo == 'Arquitectonica') and (distancia is not None):
                    if distancia < minar:
                        minar = distancia
                        minarbolar = nodo
                elif (value[0].tipo == 'Natural') and (distancia is not None):
                    if distancia < minnat:
                        minnat = distancia
                        minarbolnat = nodo

print(f'Arbol de expansion minimo de las Maravillas Arquitectonicas: {minarbolar}')
print(f'Arbol de expansion minimo de las Maravillas Naturales: {minarbolnat}')
