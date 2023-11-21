#1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
#de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
#tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
#   a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
#   b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
#       último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
#       mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
#       caracteres–;
#   c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
#   d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
#       además un listado por nivel por nombre;
#   e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
#   f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

from arbol import BinaryTree
from Cola import Cola

arbolnombre = BinaryTree()
arbolnumero = BinaryTree()
arboltipo = BinaryTree()

lista_pokemones = [{'Nombre': 'Pikachu', 'Numero': 12, 'Tipo': 'electrico'},
                  {'Nombre': 'Squirtle', 'Numero': 15, 'Tipo': 'agua'},
                  {'Nombre': 'Bulbasaur', 'Numero': 1, 'Tipo': 'planta'}]

for pokemon in lista_pokemones:
    nombre = pokemon['Nombre']
    numero = pokemon['Numero']
    tipo = pokemon['Tipo']
    
    arbolnombre.insert_node(nombre, {'Numero': numero, 'Tipo': tipo})
    arbolnumero.insert_node(numero, {'Nombre': nombre, 'Tipo': tipo})
    arboltipo.insert_node(tipo, {'Nombre': nombre, 'Numero': numero})

nom = input()

arbolnombre.search_by_coincidence(nom)


num = int(input())

pos = arbolnumero.search(num)
if pos:
    print('valor encontrado',pos.value,' ', pos.other_values)
    

tipos = ['agua', 'fuego', 'planta', 'electrico']
for tipo in tipos:
    print(f'Pokemons de tipo: {tipo}')
    arboltipo.inorden_kokemon(tipo)

print()