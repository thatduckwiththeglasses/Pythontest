

class Cola():
    def __init__(self):
        self.__datos = []
    
    def arrive(self, dato):
        self.__datos.append(dato)
        pass
    
    def atention(self):
        if len(self.__datos)== 0:
            pass
        else:
            dato = self.__datos.pop(0)
            return dato

    def size(self):
        return len(self.__datos)
    
    def empty(self):
        if self.size() == 0:
            return True
        else:
            return False
    
    def on_front(self):
        if self.size() > 0:
            return self.__datos[0]
    
    def motoend(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            
    