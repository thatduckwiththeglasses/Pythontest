class Lista():

    def __init__(self):
        self.elements = []
        
    def insertr(self,value):
        if len(self.elements) == 0:
            self.elements.append(value)
        elif value < self.elements[0]:
            self.elements.insert(0,value)
        elif value >= self.elements[-1]:
            self.elements.append(value)
        else:
            index = 1
            while value > self.elements[index]:
                index += 1
            self.elements.insert(index,value)
            
    def search(self, search_value):
        pri = 0
        ult = len(self.elements)-1
        pos = None
        mid = 0
        while (pos == None) and (pri <= ult) and (mid <= ult):
            mid = (pri + ult// 2)
            if search_value == self.elements[mid]:
                pos = mid
            elif search_value > self.elements[mid]:
                pri = mid
            elif search_value < self.elements[mid]:
                ult = mid
        return pos
    
    def delete(self,value):
        return_value = None
        pos = self.search(value)
        if pos != None:
            return_value = self.elements.pop(pos)
        return return_value
    
    def size(self):
        return len(self.elements)
    
    def barrido(self):
        for value in self.elements:
            print(value)
        