#   6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
#       casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias
#       para poder realizar las siguientes actividades:
#       
#           a. eliminar el nodo que contiene la información de Linterna Verde;
#           b. mostrar el año de aparición de Wolverine;
#           c. cambiar la casa de Dr. Strange a Marvel;
#           d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
#               “traje” o “armadura”;
#           e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
#               sea anterior a 1963;
#           f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
#           g. mostrar toda la información de Flash y Star-Lord;
#           h. listar los superhéroes que comienzan con la letra B, M y S;
#           i. determinar cuántos superhéroes hay de cada casa de comic.

from Lista import Lista

class Personaje():

    def __init__(self, nombre, ada, casa, biografia):
        self.nombre = nombre
        self.ada = ada
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados}-cbg{self.cb_ganadas}-cbp{self.cb_perdidas}'
    
sp1 = Personaje('Linterna Verde', 1960, 'DC', 'blah')
sp2 = Personaje('Wolverine', 1980, 'Marvel', 'blah')
sp3 = Personaje('Dr. Strange', 1970, 'DC', 'traje')
sp4 = Personaje('BatMan', 1960, 'DC', 'traje')
sp5 = Personaje('Iron Man', 1960, 'Marvel', 'armadura')
sp6 = Personaje('Robin', 1960, 'DC', 'blah')
sp7 = Personaje('Mujer Maravilla', 1960, 'DC', 'blah')

supers = [sp1, sp2, sp3, sp4, sp5, sp6, sp7]

lista_supers = Lista()

for super in supers:
    lista_supers.insert(super, 'nombre')

#! A
lista_supers.delete('Linterna Verde')