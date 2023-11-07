def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        # print('es un primitivo')
        return value
    else:
        # print('no es un dato primitivo')
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')


class Lista():

    def __init__(self):
        self.__elements = []
        
    def insert(self,value,criterio=None):
        if len(self.__elements) == 0 or criterio_comparacion(value,criterio) >= criterio_comparacion(self.__elements[-1],criterio):
            self.__elements.append(value)
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0], criterio):
            self.__elements.insert(0,value)
        else:
            index = 1
            while criterio_comparacion(value, criterio) > criterio_comparacion(self.__elements[index], criterio):
                index += 1
            self.__elements.insert(index,value)
    
    def search(self, search_value, criterio = None):
        pri = 0
        ult = self.size()-1
        pos = None
        while (pos == None) and (pri <= ult):
            mid = ((pri + ult)// 2)
            if search_value == criterio_comparacion(self.__elements[mid], criterio):
                pos = mid
            elif search_value > criterio_comparacion(self.__elements[mid],criterio):
                pri = mid + 1
            elif search_value < criterio_comparacion(self.__elements[mid],criterio):
                ult = mid - 1
        return pos
    
    def search_r(self, search_value, first, last, criterio = None):
        mid = ((first + last)// 2)
        if first > last:
            return None
        elif search_value == criterio_comparacion(self.__elements[mid], criterio):
            return mid
        elif search_value > criterio_comparacion(self.__elements[mid],criterio):
            return self.search_r(search_value, mid+1, last, criterio)
        elif search_value < criterio_comparacion(self.__elements[mid],criterio):
            return self.search_r(search_value, first, mid-1, criterio)
    
    def delete(self,value):
        return_value = None
        pos = self.search(value)
        if pos != None:
            return_value = self.__elements.pop(pos)
        return return_value
    
    def size(self):
        return len(self.__elements)
    
    def barrido(self):
        for value in self.__elements:
            print(value)
    
    def get_element_by_index(self,index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value
    
    def get_element_by_value(self,value):
        return_value = None
        pos = self.search(value)
        if pos:
            return_value = self.__elements[pos]
        return return_value
    
    def set_value(self, value, new_value):
        pos = self.search(value)
        if pos != None:
            value = self.delete(value)
            self.insert(new_value)
    
    