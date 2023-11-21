
from arbol import BinaryTree

arbol = BinaryTree()

print(arbol.root)
arbol.insert_node('H')
arbol.insert_node('M')
arbol.insert_node('D')
arbol.insert_node('R')
arbol.insert_node('L')
arbol.insert_node('P')
arbol.insert_node('Q')
arbol.insert_node('F')
arbol.insert_node('A')

# arbol.preorden()
print()
pos = arbol.search('A')
print(pos.value)
if pos:
    print('valor encontrado', pos.value)