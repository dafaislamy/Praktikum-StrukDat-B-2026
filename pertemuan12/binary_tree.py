class Node: #deklarasi class Node dengan isi data, left dan right
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree: #deklarasi class BinaryTree
    def __init__(self):
        self.root = None

    def insert_manual(self): #deklarasi fungsi insert_manual untuk memasukkan data satu per satu kedalam tree
        self.root = Node("A") #Node A menjadi root dalam tree (level 0)

        self.root.left = Node("B") #Node B terletak di sebelah kiri root (level 1)
        self.root.right = Node("C") #Node C terletak di sebelah kanan root (level 1)

        self.root.left.left = Node("D") #Node D terletak di sebelah kiri Node B (level 2)
        self.root.left.right = Node("E") #Node E terletak di sebelah kanan Node B (level 2)

        self.root.right.right = Node("F") #Node F terletak di sebelah kanan Node C (level 2), bagian kiri Node C kosong


def traverse_preorder(node): #preorder akan mengunjungi tree mulai dari root - left - right
    if node is not None:
        print(node.data, end=" ")
        traverse_preorder(node.left)
        traverse_preorder(node.right)

def traverse_inorder(node): #inorder akan mengunjungi tree mulai dari left - root - right
    if node is not None:
        traverse_inorder(node.left)
        print(node.data, end=" ")
        traverse_inorder(node.right)

def traverse_postorder(node): #postorder akan mengunjungi tree mulai dari left - right - root
    if node is not None:
        traverse_postorder(node.left)
        traverse_postorder(node.right)
        print(node.data, end=" ")

def get_leaf_nodes(node): #fungsi ini berguna untuk menampilkan node yang merupakan leaf (node yang tidak memiliki anak) didalam tree
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