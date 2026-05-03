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

binary_tree.insert_root("F")

binary_tree.insert_left(binary_tree.root, "B")
binary_tree.insert_right(binary_tree.root, "G")

binary_tree.insert_left(binary_tree.root.left, "A")
binary_tree.insert_right(binary_tree.root.left, "D")

binary_tree.insert_left(binary_tree.root.left.right, "C")
binary_tree.insert_right(binary_tree.root.left.right, "E")

binary_tree.insert_right(binary_tree.root.right, "I")

binary_tree.insert_left(binary_tree.root.right.right, "H")

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=" ")
        in_order(node.right)

def pre_order(node):
    if node is not None:
        print(node.data, end=" ")
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end=" ")

in_order(binary_tree.root)
print()
pre_order(binary_tree.root)
print()
post_order(binary_tree.root)