#   Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno,
#   desarrollar las funciones necesarias para resolver las siguientes actividades:
#       a. mostrar los nombre películas estrenadas en el año 2014;
#       b. indicar cuántas películas se estrenaron en el año 2018;
#       c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

from Pila import Pila

class Pelicula():

    def __init__(self, title, year, studio):
        self.__title = title
        self.__year = year
        self.__studio = studio
    
    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_studio(self):
        return self.__studio


pelis = [
        Pelicula('iron man', 2008,'marvel studios'),
        Pelicula('iron man', 2010,'marvel studios'),
        Pelicula('capitan america', 2011,'marvel studios'),
        Pelicula('shrek', 2001,'dreamworks'),
        Pelicula('madagascar', 2005,'dreamworks'),
        Pelicula('fury', 2014,'crave films'),
        Pelicula('deadpool 2', 2018,'marvel studios'),
        Pelicula('extincion', 2018,'universal pictures'),
        Pelicula('capitan america: civil war', 2016,'marvel studios'),
        Pelicula('los ilucionistas 2', 2016,'tik films')
        ]

pila = Pila()
pila2 = Pila()

for peli in pelis:
    pila.apilar(peli)

while pila.size() > 0:
    dato = pila.desapilar()
    if dato.get_year() == 2014:
        print(dato.get_title(), 'se estreno en el 2014')
    pila2.apilar(dato)

cant = 0

while pila2.size() > 0:
    dato = pila2.desapilar()
    if dato.get_year() == 2018:
        cant += 1
    pila.apilar(dato)

print(f'cantidad de peliculas estrenadas en el año 2018: {cant}')

while pila.size() > 0:
    dato = pila.desapilar()
    if (dato.get_year() == 2016) and (dato.get_studio() == 'marvel studios'):
        print(dato.get_title(), dato.get_year(), dato.get_studio())
    pila2.apilar(dato)