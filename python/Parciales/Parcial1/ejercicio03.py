#3. Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
#   cual se almacenaban en una pila en cada misión de caza que
#   emprendió (con la siguiente información planeta visitado, a quien
#   capturado, costo de la recompensa), resolver las siguientes
#   actividades:
#       a. Mostrar los planetas visitados en el orden hizo las misiones.
#       b. Determinar cuántos créditos galácticos recaudo en total.
#       c. Determinar el número de la misión en que capturo a Han Solo
#           y en que planeta fue, suponga que dicha misión está cargada.

from Pila import Pila

class mision():
    
    def __init__(self, planet, capture, bounty):
        self.__planet = planet
        self.__capture = capture
        self.__bounty = bounty
        
    def get_planet(self):
        return self.__planet

    def get_capture(self):
        return self.__capture
    
    def get_bounty(self):
        return self.__bounty
    
lista = [mision('Omicron Persei 8','Lrrr',4500)
         ,mision('Saturno','Han Solo',9000000)
         ,mision('Xen','Adrian Shepard',10000)
         ,mision('Mercurio','Jack',900)
         ,mision('Planeta X','Marvin',500)]

bitacora = Pila()
backup = Pila()

for list in lista:
    bitacora.stack(list)

while bitacora.size() > 0:
    backup.stack(bitacora.pop())

ac_cg = 0

print('Planetas Visitados:')

while backup.size() > 0:
    valor = backup.pop()
    bitacora.stack(valor)
    print(valor.get_planet())
    ac_cg += valor.get_bounty()
    

print(f'Creditos Galacticos reacudados: {ac_cg}')

total = bitacora.size()

while bitacora.size() > 0:
    valor = bitacora.pop()
    if valor.get_capture() != 'Han Solo':
        total -= 1
    else:
        print(f'Han Solo fue capturado en la mision n°{total} en el planeta {valor.get_planet()}')