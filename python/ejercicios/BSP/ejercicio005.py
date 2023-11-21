#5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
#(MCU), desarrollar un algoritmo que contemple lo siguiente:
#   a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
#       que indica si es un héroe o un villano, True y False respectivamente;
#   b. listar los villanos ordenados alfabéticamente;
#    c. mostrar todos los superhéroes que empiezan con C;
#   d. determinar cuántos superhéroes hay el árbol;
#   e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#       encontrarlo en el árbol y modificar su nombre;
#   f. listar los superhéroes ordenados de manera descendente;
#   g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#       los villanos, luego resolver las siguiente tareas:
#           I. determinar cuántos nodos tiene cada árbol;
#           II. realizar un barrido ordenado alfabéticamente de cada árbol.

from arbol import BinaryTree
from Cola import Cola

arbol = BinaryTree()

lista_personajes = [{'Nombre': 'Iron Man', 'Superheroe': True},
                    {'Nombre': 'Spider Man', 'Superheroe': True},
                    {'Nombre': 'Hulk', 'Superheroe': True},
                    {'Nombre': 'Loki', 'Superheroe': False},
                    {'Nombre': 'Dok Strange', 'Superheroe': True},]

for personaje in lista_personajes:
    arbol.insert_node(personaje['Nombre'],personaje['Superheroe'])

arbol.inorden_super_or_villano(False)
print()
arbol.inorden_start_with('R')
print()
print('cantidad de superheroes', arbol.contar_heroes())
print()
arbol.search_by_coincidence('do')

value = input('ingrese el nombre que desea modificar ')
pos = arbol.search(value)
if pos:
    is_hero = pos.other_values
    arbol.delete_node(value)
    print('modificar')
    new_value = input('ingrese en nuevo nombre ')
    arbol.insert_node(new_value, is_hero)
else:
    print('no esta')
print()
arbol.inorden()

arbol.by_level()

arbolheroes = BinaryTree()
arbolvillanos = BinaryTree()

cola = arbol.get_by_level()

for i in range(cola.size()):
    root = cola.atention()
    if root.other_values is True:
        arbolheroes.insert_node(root.value, root.other_values)
    else:
        arbolvillanos.insert_node(root.value, root.other_values)

print('Tamaño del arbol de supers: ',arbolheroes.contar_heroes())
print()
print('Tamaño del arbol de villanos: ',arbolvillanos.contar_villanos())
print()

arbolheroes.inorden()
print()
arbolvillanos.inorden()