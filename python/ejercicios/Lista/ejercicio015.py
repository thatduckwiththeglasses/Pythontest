#   15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad
#de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además
#la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
#las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
#
#       a. obtener la cantidad de Pokémons de un determinado entrenador;
#       b. listar los entrenadores que hayan ganado más de tres torneos;
#       c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
#       d. mostrar todos los datos de un entrenador y sus Pokémos;
#       e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
#       f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
#           (tipo y subtipo);
#       g. el promedio de nivel de los Pokémons de un determinado entrenador;
#       h. determinar cuántos entrenadores tienen a un determinado Pokémon;
#       i. mostrar los entrenadores que tienen Pokémons repetidos;
#       j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
#           o Wingull;
#       k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#           como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
#           deberán mostrar los datos de ambos;

from Listadelista import Lista
from random import randint

class Entrenador():

    def __init__(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados}-cbg{self.cb_ganadas}-cbp{self.cb_perdidas}'

class Pokemon():

    def __init__(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}'


e1 = Entrenador('Juan', ct_ganados=randint(1, 10))
e2 = Entrenador('Maria', ct_ganados=randint(1, 10))
e3 = Entrenador('Ana', ct_ganados=randint(1, 10))

entrenadores = [e1, e2, e3]

lista_entrenadores = Lista()

p1 = Pokemon('pikachu', 'electrico', randint(1, 20))
p2 = Pokemon('jolteon', 'electrico', randint(1, 20))
p3 = Pokemon('vaporeon', 'agua', randint(1, 20))
p4 = Pokemon('flareon', 'fuego', randint(1, 20))
p5 = Pokemon('leafeon', 'planta', randint(1, 20))

pokemons = [p1, p2, p3, p4, p5]

#! lista principal
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

#! lista secundaria
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


lista_entrenadores.barrido()
print()

#! A
pos = lista_entrenadores.search('Juan', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

print()
#! B
lista_entrenadores.barrido_cantidad_torneos_ganados(3)

print()
#! C
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
pos_mayor = 0

for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.ct_ganados

valor = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = valor[0], valor[1]

if sublista.size() > 0:
    pokemon_mayor = sublista.get_element_by_index(0)
    for pos in range(1, sublista.size()):
        pokemon = sublista.get_element_by_index(pos)
        if pokemon.nivel > pokemon_mayor.nivel:
            pokemon_mayor = pokemon
    print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} {pokemon_mayor.nivel} ')
else:
    print(f'No se pudo encontrar un mayor')
print()

#! D
pos = lista_entrenadores.search('Maria', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons:')
    for i in range(0, sublista.size()):
        valor2 = sublista.get_element_by_index(i)
        print(valor2)
print()

#! E
lista_entrenadores.barrido_porcentaje_batallas_ganadas(79)

#! F
for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)
    sublista = entrenador[1]
    for i in range(0, sublista.size()):
        valor = sublista.get_element_by_index(i)
        if ((valor.tipo == 'fuego') and (valor.tipo == 'planta')) or (valor.tipo == 'agua'):
            print(entrenador[0].nombre)
print()

#! G
entrenador_nombre = input('Ingrese el nombre del entrenador:')
pos = lista_entrenadores.search(entrenador_nombre, 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    total = 0
    for i in range(0, sublista.size()):
        valor2 = sublista.get_element_by_index(i)
        total = total + valor2.nivel
        print(total / sublista.size())
print()

#! H

