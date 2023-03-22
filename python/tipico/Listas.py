#Listas
demo_list = [23,'Que',3.54,False,[3,4,5]]
print(demo_list)
print(type(demo_list))

#list(), Crea una lista
number_list = list((2,1,45,4))
print(number_list)

r = list(range(1,10))
print(r)

#print(dir(demo_list))
print(len(demo_list))

#Buscar si se encuentra un valor en la lista
print('que' in demo_list)

#modificar un valor de la lista
demo_list[1] = 'que'
print('que' in demo_list)

#Añade un valor a la lista
demo_list.append('hola')
print(demo_list)

#Añade mas de un valor solo como listas o tuplas
demo_list.extend(['adios',13])
print(demo_list)

#Añade un valor en un espacio definido
demo_list.insert(1, 'violeta')
print(demo_list)

#Saca un valor de la lista
demo_list.pop() #<- el ultimo valor
demo_list.pop(2) # <-un valor en esta posicion
print(demo_list)

#Saca un determinado elemento de la lista
demo_list.remove('violeta')
print(demo_list)

#Limpia la lista
#demo_list.clear()
print(demo_list)

#Ordena la lista
number_list.sort()
number_list.sort(reverse=True) #Ordena de forma inversa
print(number_list)
