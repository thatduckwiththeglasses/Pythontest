#10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
#     de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
#     resolver las siguientes actividades:
#       a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#       b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
#           la palabra ‘Python’, sin perder datos en la cola;
#       c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
#           11:43 y las 15:57, y determinar cuántas son.

from Cola import Cola
from Pila import Pila

class noti():
    
    def __init__(self,red,h,mesg):
        self.__red = red
        self.__h = h
        self.__mesg = mesg
    
    def get_red(self):
        return self.__red

    def get_hour(self):
        return self.__h

    def get_mesg(self):
        return self.__mesg
    
cola = Cola()
pila = Pila()

cola.arrive(noti('Twitter','11:43','Python'))
cola.arrive(noti('Twitter','12:29','New Follow'))
cola.arrive(noti('Facebook','11:43','Friends'))
cola.arrive(noti('Twitter','20:49','Twit Response'))
cola.arrive(noti('Facebook','10:30','Recommendation'))
cola.arrive(noti('Instagram','09:47','New Photos'))

total = cola.size()
i = 0

print('Punto B:')
while total > i:
    valor = cola.atention()
    if (valor.get_red() == 'Twitter') and (valor.get_mesg().find('Python') != -1):
        print(valor.get_red(),valor.get_mesg(),valor.get_hour())
    cola.arrive(valor)
    i += 1

i = 0

cont = 0
print('Punto C:')
while total > i:
    valor = cola.atention()
    if (valor.get_hour() >= '11:43') and (valor.get_hour() <= '15:57'):
        print(valor.get_red(),valor.get_mesg(),valor.get_hour())
        pila.apilar(valor)
        cont += 1
    cola.arrive(valor)
    i += 1

print(f'Son {cont} notificaciones entre 11:43 y las 15:57')

i = 0
print('Punto A:')
while total >= i:
    valor = cola.atention()
    if (valor.get_red().find('Facebook') == -1):
        cola.arrive(valor)
    else:
        print(valor.get_red(),valor.get_mesg(),valor.get_hour(),i)
        total -= 1
    i += 1

print('Cola:')
while cola.size() > 0:
    valor = cola.atention()
    print(valor.get_red(),valor.get_mesg(),valor.get_hour())

print('Pila:')
while pila.size() > 0:
    valor = pila.desapilar()
    print(valor.get_red(),valor.get_mesg(),valor.get_hour())