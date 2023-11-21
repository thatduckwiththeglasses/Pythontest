#23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
#   resuelva las siguientes consultas:
#
#   a. listado inorden de las criaturas y quienes la derrotaron;
#   b. se debe permitir cargar una breve descripción sobre cada criatura;
#   c. mostrar toda la información de la criatura Talos;
#   d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
#   e. listar las criaturas derrotadas por Heracles;
#   f. listar las criaturas que no han sido derrotadas;
#   g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
#       o dios que la capturo;
#   h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#       Erimanto indicando que Heracles las atrapó;
#   i. se debe permitir búsquedas por coincidencia;
#   j. eliminar al Basilisco y a las Sirenas;
#   k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#       derroto a varias;
#   l. modifique el nombre de la criatura Ladón por Dragón Ladón;
#   m. realizar un listado por nivel del árbol;
#   n. muestre las criaturas capturadas por Heracles.

from arbol import BinaryTree

arbol = BinaryTree()

lista_personajes = [{'critter': 'Ceto', 'info': ' ', 'defeat': ' ', 'capture': ' '},
                    {'critter': 'Tifón', 'info': ' ', 'defeat': 'Zeus', 'capture': ' '},
                    {'critter': 'Equidna', 'info': ' ', 'defeat': 'Argos Panoptes', 'capture': ' '},
                    {'critter': 'Dino', 'info': ' ', 'defeat': ' ', 'capture': ' '},
                    {'critter': 'Pefredo', 'info': ' ', 'defeat': ' ', 'capture': ' '},
                    {'critter': 'Enio', 'info': ' ', 'defeat': ' ', 'capture': ' '},
                    {'critter': 'Escila', 'info': ' ', 'defeat': ' ', 'capture': ' '},
                    {'critter': 'Caribdis', 'info': ' ', 'defeat': ' ', 'capture': ' '},
                    {'critter': 'Euríale', 'info': ' ', 'defeat': ' ', 'capture': ' '},
                    {'critter': 'Esteno', 'info': ' ', 'defeat': ' ', 'capture': ' '},
                    {'critter': 'Medusa', 'info': ' ', 'defeat': 'Perseo', 'capture': ' '},
                    {'critter': 'Ladón', 'info': ' ', 'defeat': 'Heracles', 'capture': ' '},
                    {'critter': 'Aguila del Cáucaso', 'info': ' ', 'defeat': ' ', 'capture': ' '},
                    {'critter': 'Quimera', 'info': ' ', 'defeat': 'Belerofonte', 'capture': ' '},
                    {'critter': 'Hidra de Lerna', 'info': ' ', 'defeat': 'Heracles', 'capture': ' '},
                    {'critter': 'León de Nemea', 'info': ' ', 'defeat': 'Heracles', 'capture': ' '},]

for personaje in lista_personajes:
    arbol.insert_node(personaje['critter'],[personaje['info'], personaje['defeat'], personaje['capture']])

#a.
arbol.inorden()

#b.
opcion = input('Desea ingresar informacion sobre las criaturas?: s para si')
while opcion == 's':
    buscar = input('Ingrese la criatura: ')
    info = input('Ingrese la informacion: ')
    pos = arbol.search_by_coincidence(buscar)
    if pos:
        arbol.insert_node(pos['critter'],[info, pos['defeat'], pos['capture']])
    opcion = input('Desea ingresar mas informacion sobre las criaturas?: s para si')

#c.    
pos = arbol.search('Talos')
if pos:
    print(pos.value)
    print(pos.other_values['info'])

#d.
max1 = 0; max2 = 0; max3 = 0
d1 = ' '; d2 = ' '; d3 = ' '
lista_op = ['Zeus','Argos Panoptes', 'Perseo','Heracles','Belerofonte']

for op in lista_op:
    value = arbol.count_defeats(op)
    if max1 < value:
        max3 = max2
        max2 = max1
        max1 = value
        d1 = op
    elif max2 < value:
        max3 = max2
        max2 = value
        d2 = op
    else:
        max3 = value
        d3 = op

print('Los heroes o dioses que mas criaturas derrotaron son: ')
print(f'1°: {d1} con {max1} criaturas derrotadas')
print(f'2°: {d2} con {max2} criaturas derrotadas')
print(f'3°: {d3} con {max3} criaturas derrotadas')
print()

#e.
print('Criaturas derrotadas por Heracles:')    
arbol.inorden_defeat('Heracles')
print()

#f.
print('Criaturas que no han sido derrotadas:')
arbol.inorden_defeat(' ')
print()

#h.
value = 'Cerbero'
pos = arbol.search(value)
if pos:
    name = pos.value
    arbol.delete_node(value)
    print('modificar')
    new_value = 'Heracles'
    arbol.insert_node(name, [pos.other_values['info'],pos.other_values['defeat'],new_value])
else:
    print('no esta')
print()

value = 'Toro de Creta'
pos = arbol.search(value)
if pos:
    name = pos.value
    arbol.delete_node(value)
    print('modificar')
    new_value = 'Heracles'
    arbol.insert_node(name, [pos.other_values['info'],pos.other_values['defeat'],new_value])
else:
    print('no esta')
print()

value = 'Cierva Cerinea'
pos = arbol.search(value)
if pos:
    name = pos.value
    arbol.delete_node(value)
    print('modificar')
    new_value = 'Heracles'
    arbol.insert_node(name, [pos.other_values['info'],pos.other_values['defeat'],new_value])
else:
    print('no esta')
print()

value = 'Jabalí de Erimanto'
pos = arbol.search(value)
if pos:
    name = pos.value
    arbol.delete_node(value)
    print('modificar')
    new_value = 'Heracles'
    arbol.insert_node(name, [pos.other_values['info'],pos.other_values['defeat'],new_value])
else:
    print('no esta')
print()

#j.
arbol.delete_node('Basilico')
arbol.delete_node('Sirenas')

#k.
value = 'Aves del Estínfalo'
pos = arbol.search(value)
if pos:
    name = pos.value
    arbol.delete_node(value)
    print('modificar')
    new_value = 'Heracles derroto a varias'
    arbol.insert_node(name, [new_value,pos.other_values['defeat'],pos.other_values['capture']])
else:
    print('no esta')
print()

#l.
value = 'Ladón'
pos = arbol.search(value)
if pos:
    info = pos.other_values
    arbol.delete_node(value)
    print('modificar')
    new_value = 'Dragon Ladón'
    arbol.insert_node(new_value, info)
else:
    print('no esta')
print()

#m.
arbol.by_level()

#n.
print('Criaturas capturadas por Heracles:')    
arbol.inorden_capture('Heracles')
print()