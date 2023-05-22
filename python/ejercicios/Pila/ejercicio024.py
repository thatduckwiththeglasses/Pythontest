# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
#   a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
#       uno la cima de la pila;
#   b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
#       la cantidad de películas en la que aparece;
#   c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#   d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from Pila import Pila

class Personaje():

    def __init__(self, name, app):
        self.__name = name
        self.__app = app
    
    def get_name(self):
        return self.__name

    def get_app(self):
        return self.__app

perso = [
    Personaje('Hulk',6),
    Personaje('Black Widow',9),
    Personaje('Groot',3),
    Personaje('Captain America',20)
    ]

pila = Pila()
pila2 = Pila()

for per in perso:
    pila.apilar(per)

pos = 1
while pila.size() > 0:
    dato = pila.desapilar()
    if dato.get_name() == 'Rocket Racoon':
        print(f'Rocket Racoon se encuentra en la posicion: {pos}')
    if dato.get_name() == 'Groot':
        print(f'Groot se encuentra en la posicion: {pos}')
    pos += 1
    pila2.apilar(dato)

while pila2.size() > 0:
    dato = pila2.desapilar()
    if dato.get_app() > 5:
        print(dato.get_name(),dato.get_app())
    pila.apilar(dato)
    
while pila.size() > 0:
    dato = pila.desapilar()
    if dato.get_name() == 'Black Widow':
        print(f'{dato.get_name()} participo en {dato.get_app()} peliculas')
    pila2.apilar(dato)

while pila2.size() > 0:
    dato = pila2.desapilar()
    if dato.get_name().startswith('C') or dato.get_name().startswith('D') or dato.get_name().startswith('G'):
        print(dato.get_name(),dato.get_app())
    pila.apilar(dato)