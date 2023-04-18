#20. Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de
#   manera recursiva, y permita determinar si un valor dado está o no en dicha lista.

lista_num = [1, 4, 5, 6, -5, 9]

def secuencial(lista,buscado):
    if len(lista) == 0:
        return -1
    elif lista[-1] == buscado:
        return len(lista)-1
    else:
        return secuencial(lista[0:-1],buscado)
    
print(secuencial(lista_num,5))