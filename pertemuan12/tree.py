'''
Tree (Pohon) adalah struktur data non-linear yang merepresentasikan
hubungan hierarkis antar elemen.

Tree terdiri dari:
- Node : elemen data dalam tree
- Edge : penghubung antar node
- Root : node paling atas (tidak memiliki parent)
- Leaf : node paling bawah (tidak memiliki child)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

binary_tree = BinaryTree()

binary_tree.insert_root(10)
binary_tree.insert_left(binary_tree.root, 5)
binary_tree.insert_right(binary_tree.root, 15)
binary_tree.insert_left(binary_tree.root.left, 3)
binary_tree.insert_right(binary_tree.root.left, 7)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=" ")
        in_order(node.right)

in_order(binary_tree.root)