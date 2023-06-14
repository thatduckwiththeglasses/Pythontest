

class Pila():
    """Stack Class"""
    def __init__(self):
        self.__datos = []
        
    def stack(self, dato):
        self.__datos.append(dato)
        pass
    
    def pop(self):
        if len(self.__datos)== 0:
            pass
        else:
            dato = self.__datos.pop()
            return dato
    
    def size(self):
        return len(self.__datos)
    
    def vacio(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def ontop(self):
        if self.size > 0:
            return self.__datos[-1]
        
    def __eq__(self, stack_aux):
        if isinstance(stack_aux,Pila):
            if self.__datos == stack_aux.__datos:
                return True
            else:
                return False
        else:
            pass