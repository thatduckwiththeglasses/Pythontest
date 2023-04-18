#21. Dada una lista de valores ordenadas, desarrollar un algoritmo que modifique el método de
#   búsqueda binaria para que funcione de forma recursiva, y permita determinar si un valor dado
#   está o no en dicha lista.

lista_num = [0,1,2,3,4,5,6,7,8,9]

def binaria(lista,buscado,pri,ult):
    if pri > ult:
        return -1
    else:
        medio = ((pri + ult) // 2)
        if lista[medio] == buscado:
            return medio
        elif buscado > lista[medio]:
            return binaria(lista,buscado,medio+1,ult)
        else:
            return binaria(lista,buscado,pri,medio-1)

print(binaria(lista_num,4,0,len(lista_num)-1))