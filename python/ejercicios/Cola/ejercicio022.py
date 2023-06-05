#22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
#    el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
#    –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc.,
#    desarrollar un algoritmo que resuelva las siguientes actividades:
#       a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#       b. mostrar los nombre de los superhéroes femeninos;
#       c. mostrar los nombres de los personajes masculinos;
#       d. determinar el nombre del superhéroe del personaje Scott Lang;
#       e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
#       f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

from Cola import Cola

class Personaje():

    def __init__(self, name, nickname, genre):
        self.__name = name
        self.__nickname = nickname
        self.__genre = genre
    
    def get_name(self):
        return self.__name

    def get_nickname(self):
        return self.__nickname
    
    def get_genre(self):
        return self.__genre

grupo = [
    Personaje('Tony Stark', 'Iron Man', 'M'),
    Personaje('Steve Rogers', 'Capitán América', 'M'),
    Personaje('Natasha Romanoff', 'Black Widow', 'F'),
    Personaje('Scott Lang', 'Ant Man', 'M'),
    Personaje('Carol Danvers', 'Capitana Marvel', 'F'),
    Personaje('Wanda Maximoff', 'Bruja Escarlata', 'F'),
    Personaje('Bruce Banner', 'Hulk', 'M'),
]

cola = Cola()

for per in grupo:
    cola.arrive(per)

i = 0
total = cola.size()

while total > i :
    valor = cola.atention()
    if valor.get_nickname() == 'Capitana Marvel':
        print(f'Nombre de Capitana Marvel: {valor.get_name()}')
    cola.arrive(valor)
    i += 1

i = 0
print('Todos los Superheores Femeninos:')
while total > i :
    valor = cola.atention()
    if (valor.get_genre() == 'F'):
        print(valor.get_nickname())
    cola.arrive(valor)
    i += 1

i = 0
print('Todos los personajes Masculinos:')
while total > i :
    valor = cola.atention()
    if (valor.get_genre() == 'M'):
        print(valor.get_name())
    cola.arrive(valor)
    i += 1
    
i = 0

while total > i :
    valor = cola.atention()
    if valor.get_name() == 'Scott Lang':
        print(f'Scott Lang alias: {valor.get_nickname()}')
    cola.arrive(valor)
    i += 1
    
i = 0

while total > i :
    valor = cola.atention()
    if (valor.get_name().startswith('S')) or (valor.get_nickname().startswith('S')):
        print(f'Nombre: {valor.get_name()}, Superheore: {valor.get_nickname()}, Genero: {valor.get_genre()}')
    cola.arrive(valor)
    i += 1

i = 0

while total > i :
    valor = cola.atention()
    if valor.get_name() == 'Carol Danvers':
        print(f'Carol Danvers si se encuentra como: {valor.get_nickname()}')
    cola.arrive(valor)
    i += 1