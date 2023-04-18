#10. Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de una
#   pila con nombres de dioses griegos

from Pila import Pila

stack = Pila()

dioses = ['Zeus','Hermes','Hera','Apolo','Poseidon','Artemisa','Afrodita','Hefesto','Ares','Demeter','Hestia']

for  i in range(11):
    stack.apilar(dioses[i])

pos = int(input('Ingrese en que posicion deveria colocar a Atenea: '))

aux = Pila()

while stack.size() >= pos:
    aux.apilar(stack.desapilar())
    
stack.apilar('Atenea')

while aux.size() > 0:
    stack.apilar(aux.desapilar())

while stack.size() > 0:
    print(stack.desapilar())