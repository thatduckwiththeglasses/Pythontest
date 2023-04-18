#22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#   otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#   objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#   ayuda de la fuerza” realizar las siguientes actividades:

#   a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#   queden más objetos en la mochila;

#   b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
#   car para encontrarlo;

#   c. Utilizar un vector para representar la mochila.

def sacar_sable(lista):
    if len(lista) > 0:
        if lista[0] == 'sable de luz':
            return 0
        else:
            print(lista.pop(0))
            return 1 + sacar_sable(lista)
    else:
        return 0
    
lista = ['libro','linterna','celular','ropa','vino','sable de luz']

print(sacar_sable(lista))
if len(lista) > 0:
    print('Se encontro el sable de luz')
else:
    print('No hay sable XD')