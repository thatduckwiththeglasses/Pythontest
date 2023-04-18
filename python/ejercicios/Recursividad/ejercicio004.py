#4. Implementar una función para calcular la potencia dado dos números enteros, el primero re-
#   presenta la base y segundo el exponente.
# 5**2 = 5 * 5 = 25



def potenciar(base,exponente):
    """Calcula la potencia de una base con un exponente ingresados (de forma recursiva)"""
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potenciar(base,exponente + 1)
    else:
        return base * potenciar(base, exponente - 1)
print(potenciar(3,5))