#1. Desarrollar una función recursiva que permita contar cuantas veces
#   aparece una determinada palabra, en un vector de palabras.

def contador(vector,palabra):
    if len(vector) == 0:
        return 0
    elif vector[-1] == palabra:
        return 1 + contador(vector[0:-1],palabra)
    else:
        return contador(vector[0:-1],palabra)
    
vec = ['arbol','auto','tele','auto','freezer','monitor','auto']

print(contador(vec,'auto'))