class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node("A")

        self.root.left = Node("B")
        self.root.right = Node("C")

        self.root.left.left = Node("D")
        self.root.left.right = Node("E")

        self.root.right.right = Node("F")


def traverse_preorder(node):
    if node is not None:
        print(node.data, end=" ")
        traverse_preorder(node.left)
        traverse_preorder(node.right)

def traverse_inorder(node):
    if node is not None:
        traverse_inorder(node.left)
        print(node.data, end=" ")
        traverse_inorder(node.right)

def traverse_postorder(node):
    if node is not None:
        traverse_postorder(node.left)
        traverse_postorder(node.right)
        print(node.data, end=" ")

def get_leaf_nodes(node):
    if node:
        if not node.left and not node.right:
            print(node.data, end=" ")
        get_leaf_nodes(node.left)
        get_leaf_nodes(node.right)


print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print("======================================")
print("[INFO] Membangun Struktur Gudang...")

binary_tree = BinaryTree()
binary_tree.insert_manual()

print("[INFO] Struktur berhasil dibuat.")
print()


print("HASIL AUDIT:")
print("1. Pre-Order  :", end=" ")
traverse_preorder(binary_tree.root)
print()

print("2. In-Order   :", end=" ")
traverse_inorder(binary_tree.root)
print()

print("3. Post-Order :", end=" ")
traverse_postorder(binary_tree.root)
print()

print("[DATA] Gudang Ujung (Leaf Nodes) :", end=" ")
get_leaf_nodes(binary_tree.root)
print()
print("======================================")
print("Audit Selesai!")