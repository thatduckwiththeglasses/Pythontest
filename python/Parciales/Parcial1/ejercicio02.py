#2. Dada una lista con nombres de personajes de la saga de Avengers
#   ordenados por nombre del superhéroes, de los cuales se conoce:
#   nombre del superhéroe, nombre del personaje (puede ser vacio),
#   grupo al que (perteneces puede ser vacio), año de aparición, por
#   ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
#   Resolver las siguientes tareas:
#       a. Determinar si “Capitana Marvel” está en la lista y mostrar su
#           nombre de personaje;
#       b. Almacenar los superhéroes que pertenezcan al grupo
#           “Guardianes de la galaxia” en una cola e indicar cuantos son.
#       c. Mostrar de manera descendente los superhéroes que
#           pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de
#           la galaxia”.
#       d. Listar los superhéroes que tengan nombre de personajes cuyo
#           año de aparición sea posterior a 1960.
#       e. Hemos detectado que la superhéroe “Black Widow” está mal
#           cargada por un error de tipeo, figura como “Vlanck Widow”,
#           modifique dicho superhéroe para solucionar este problema.
#       f. Dada una lista auxiliar con los siguientes personajes (‘Black
#           Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la
#           información), agregarlos a la lista principal en el caso de no
#           estar cargados.
#       g. Mostrar todos los personajes que comienzan con C, P o S.
#       h. Cargue al menos 20 superheroes a la lista.

from Lista import Lista
from Cola import Cola
from Pila import Pila

class Personaje():

    def __init__(self, nickname, name, group, year):
        self.name = name
        self.nickname = nickname
        self.group = group
        self.year = year
        
    def get_name(self):
        return self.name

    def get_nickname(self):
        return self.nickname
    
    def get_group(self):
        return self.group
    
    def get_year(self):
        return self.year
    
    def __str__(self) -> str:
        return f'{self.nickname} - {self.name} - {self.group} - {self.year}'
    
listap = [Personaje('Star Lord','Peter Quill', 'Guardianes de la galaxia', 1976)
        ,Personaje('Iron Man','Tony Stark', 'Los Vengadores', 1963)
        ,Personaje('Vlanck Widow','Natasha Romanoff', 'Los Vengadores', 1964)
        ,Personaje('Capitana Marvel','Carol Danvers', 'Los Vengadores', 1968)
        ,Personaje('Antorcha Humana',' ', 'Los Cuatros Fantasticos', 1961)
        ,Personaje('Groot',' ', ' ', 1960)
        ,Personaje('Hulk',' ', 'Los Vengadores', 1961)
        ,Personaje('Loki',' ', 'Dioses', 1961)
        ,Personaje('La Roca',' ', 'Los Cuatros Fantasticos', 1961)
        ,Personaje('Rocket Racoonn',' ', 'Guardianes de la galaxia', 1961)
        ,Personaje('Black Cat',' ', 'Aparte', 1961)
        ,Personaje('Capitan America',' ', 'Los Vengadores', 1961)
        ,Personaje('Mr. Fantastico',' ', 'Los Cuatros Fantasticos', 1961)
        ,Personaje('Mujer Invisible',' ', 'Los Cuatros Fantasticos', 1961)
        ,Personaje('Ant Man',' ', 'Los Vengadores', 1961)
        ,Personaje('Spider Man',' ', 'Los Vengadores', 1961)
        ,Personaje('Thor',' ', 'Los Vengadores', 1961)
        ,Personaje('DeadPool',' ', 'aparte', 1961)
        ,Personaje('Dante',' ', 'Devil May Cry', 2001)
        ,Personaje('GwenPool',' ', 'aparte', 1961)]

lista1 = Lista()

for list in listap:
    lista1.insertr(list,'nickname')

# Punto a:

pos = lista1.search_r('Capitana Marvel',0,lista1.size(),'nickname')
nombre = lista1.get_element_by_index(pos)

if pos is not None:
    print(f'Capitana Marvel si esta en la lista: {nombre}')
    print()

#Punto b:
    
cola = Cola()

lista1.order_by('group')

pos = lista1.search_r('Guardianes de la galaxia',0,lista1.size(),'group')
perso = lista1.get_element_by_index(pos)
while perso.get_group() == 'Guardianes de la galaxia':
    cola.arrive(perso)
    pos += 1
    perso = lista1.get_element_by_index(pos)

print(f'Los Guardianes de la galaxia son: {cola.size()}')
print()

#Punto c:

lista1.order_by('nickname',True)

i = 0
print('Pertenecen a Los Guardianes o los 4 fantasticos: ')
while i <= lista1.size()-1:
    perso = lista1.get_element_by_index(i)
    if (perso.get_group() == 'Guardianes de la galaxia') or (perso.get_group() == 'Los Cuatros Fantasticos'):
        print(perso.__str__())
    i += 1
print()
#Punto d:
    
i = 0
print('Personajes con nombre que aparecieron despues de 1960:')
while i <= lista1.size()-1:
    perso = lista1.get_element_by_index(i)
    if ((perso.get_name() != '') or (perso.get_name() is not None)) and (perso.get_year() > 1960):
        print(perso.__str__())
    i += 1
print()   
#Punto e:

valor = lista1.delete('Vlanck Widow','nickname')
if valor is not None:
    lista1.insertr(Personaje('BlaCk Widow','Natasha Romanoff', 'Los Vengadores', 1964),'nickname')

#Punto f:

pila = Pila()

lista = [Personaje('Hulk',' ', 'Los Vengadores', 1961)
        ,Personaje('Rocket Racoonn',' ', 'Guardianes de la galaxia', 1961)
        ,Personaje('Black Cat',' ', 'Aparte', 1961)
        ,Personaje('Loki',' ', 'Dioses', 1961)]

for list in lista:
    pila.stack(list)

pos = lista1.search('Loki','nickname')
if pos is None:
    lista1.insertr(pila.pop(),'nickname')
pos = lista1.search('LBlack Cat','nickname')
if pos is None:
    lista1.insertr(pila.pop(),'nickname')
pos = lista1.search('Rocket Racoonn','nickname')
if pos is None:
    lista1.insertr(pila.pop(),'nickname')
pos = lista1.search('Hulk','nickname')
if pos is None:
    lista1.insertr(pila.pop(),'nickname')

#Punto g: 

i = 0
print('Personajes cuyo nombre empiezan con "C", "P", o "S":')
while i <= lista1.size()-1:
    perso = lista1.get_element_by_index(i)
    
    if perso.get_nickname().startswith('C') or perso.get_nickname().startswith('P') or perso.get_nickname().startswith('S'):
        print(perso.__str__())
    i += 1