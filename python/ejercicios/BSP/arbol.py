
from Cola import Cola
import linecache


def get_value_from_file(file_name, index):
    line = linecache.getline(file_name, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split

class NodeTree():

    def __init__(self, value, other_values=None):
        self.value = value
        self.other_values = other_values
        self.left = None
        self.right = None
        self.height = 0

class BinaryTree:

    def __init__(self):
        self.root = None
    
    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_values=None):

        def __insertar(root, value, other_values):
            if root is None:
                return NodeTree(value, other_values)
            elif value < root.value:
                root.left = __insertar(root.left, value, other_values)
            else:
                root.right = __insertar(root.right, value, other_values)
            print('izquierda', self.height(root.left) - self.height(root.right))
            print('derecha', self.height(root.right) - self.height(root.left))
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values)

    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(node.value)
                # a = input()
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                if root.other_values:
                    print(root.other_values)
                __inorden(root.right)

        __inorden(self.root)
 
    def inorden_file(self, file_name):
        def __inorden_file(root, file_name):
            if root is not None:
                __inorden_file(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                print(root.value, value[0])
                __inorden_file(root.right, file_name)

        __inorden_file(self.root, file_name)
 
    
    def inorden_start_with(self, cadena):
        def __inorden_start_with(root, cadena):
            if root is not None:
                __inorden_start_with(root.left, cadena)
                if root.other_values is True and root.value.upper().startswith(cadena):
                    print(root.value,root.other_values)
                __inorden_start_with(root.right, cadena)

        __inorden_start_with(self.root, cadena)

    def inorden_kokemon(self, tipo):
        def __inorden_start_with(root, tipo):
            if root is not None:
                __inorden_start_with(root.left, tipo)
                if tipo in root.value:
                    print(root.value,root.other_values)
                __inorden_start_with(root.right, tipo)

        __inorden_start_with(self.root, tipo)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value, root.height)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)
        
    def search_by_coincidence(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value,root.other_values)
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node
        
        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
            return root, value
        
        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value
    
    def count(self, value):
        count1 = 0
        def __count(root,value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                elif root.left is not None:
                    return count + __count(root.left, value)
                elif root.right is not None:
                    return count + __count(root.right, value)
                else:
                    return 0
            return count
                
        count1 = __count(self.root, value)
        return count1
    
    def inorden_file_lightsaber(self, file_name, lightsaber_color):
        def __inorden_file_lightsaber(root, file_name, lightsaber_color):
            if root is not None:
                __inorden_file_lightsaber(root.left, file_name, lightsaber_color)
                value = get_value_from_file(file_name, root.other_values)
                if lightsaber_color in value[4].split('/'):
                    print(root.value, value[4].split('/'))
                __inorden_file_lightsaber(root.right, file_name, lightsaber_color)

        __inorden_file_lightsaber(self.root, file_name, lightsaber_color)
    
    def inorden_file_species(self, file_name, lightsaber_color):
        def __inorden_file_lightsaber(root, file_name, lightsaber_color):
            if root is not None:
                __inorden_file_lightsaber(root.left, file_name, lightsaber_color)
                value = get_value_from_file(file_name, root.other_values)
                if lightsaber_color in value[3].split('/'):
                    print(root.value, value[3].split('/'))
                __inorden_file_lightsaber(root.right, file_name, lightsaber_color)

        __inorden_file_lightsaber(self.root, file_name, lightsaber_color)
    
    def inorden_start_with_jedi(self, cadena):
        def __inorden_start_with_jedi(root, cadena):
            if root is not None:
                __inorden_start_with_jedi(root.left, cadena)
                if root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with_jedi(root.right, cadena)

        __inorden_start_with_jedi(self.root, cadena)
        
    def inorden_has_jedi(self, cadena):
        def __inorden_start_with_jedi(root, cadena):
            if root is not None:
                __inorden_start_with_jedi(root.left, cadena)
                if root.value.upper().find(cadena):
                    print(root.value)
                __inorden_start_with_jedi(root.right, cadena)

        __inorden_start_with_jedi(self.root, cadena)
    
    def inorden_super_or_villano(self, is_hero):
        def __inorden_s_v(root, is_hero):
            if root is not None:
                __inorden_s_v(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden_s_v(root.right, is_hero)

        __inorden_s_v(self.root, is_hero)

    def contar_heroes(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is True:
                    count = 1
                count += __contar_heroes(root.left)
                count += __contar_heroes(root.right)
            return count
     
    def contar_villanos(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is False:
                    count = 1
                count += __contar_heroes(root.left)
                count += __contar_heroes(root.right)
            return count
        
    def inorden_capture(self, is_capture):
        def __inorden_c(root, is_capture):
            if root is not None:
                __inorden_c(root.left, is_capture)
                if root.other_values[2] is is_capture:
                    print(root.value)
                __inorden_c(root.right, is_capture)

        __inorden_c(self.root, is_capture)
    
    def inorden_defeat(self, is_capture):
        def __inorden_c(root, is_capture):
            if root is not None:
                __inorden_c(root.left, is_capture)
                if root.other_values[1] is is_capture:
                    print(root.value)
                __inorden_c(root.right, is_capture)

        __inorden_c(self.root, is_capture)
        
    def count_defeats(self, oponent):
        count1 = 0
        def __count_defeats(root):
            count = 0
            if root is not None:
                if root.other_values[1] is oponent:
                    count = 1
                count += __count_defeats(root.left)
                count += __count_defeats(root.right)
            return count
        count1 = __count_defeats(self.root)
        return count1
    
    def list_defeat(self):
        lista = []
        def __count_defeats(root):
            lista = []
            if root is not None:
                if root.other_values[1] is not ' ' and root.other_values[1] is not lista[-1]:
                    lista.append(root.other_values[1])
                __count_defeats(root.left)
                __count_defeats(root.right)
            return lista
    
    def get_by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            if self.root.left is not None:
                cola_tree.arrive(self.root.left)
            if self.root.right is not None:
                cola_tree.arrive(self.root.right)
        return cola_tree