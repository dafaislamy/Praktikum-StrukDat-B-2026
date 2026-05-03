class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)
        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return
        
        current = self.root
        while True:
            if id_buku < current.id_buku:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left

            if id_buku > current.id_buku:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    def search(self, id_buku):
        current = self.root
        while current is not None:
            if id_buku == current.id_buku:
                return current
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right
        return None

    def traversal_inorder(self, node):
        if node:
            self.traversal_inorder(node.left)
            print(f"{node.id_buku} - {node.judul}")
            self.traversal_inorder(node.right)

    def get_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.id_buku

    def get_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.id_buku

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1


print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print("=========================================")
print()

binary_search_tree = BinarySearchTree()

buku = [(50, "Dasar Pemrograman"),
        (30, "Struktur Data"),
        (70, "Kecerdasan Buatan"),
        (20, "Matematika Diskrit"),
        (40, "Basis Data"),
        (60, "Jaringan Komputer"),
        (80, "Sistem Operasi")]

for id, nama in buku:
    binary_search_tree.insert(id, nama)
print()

print("[INFO] Koleksi Buku (In-Order Traversal):")
binary_search_tree.traversal_inorder(binary_search_tree.root)
print()


print("[SEARCH] Mancari ID 60...", end=" ")
cari1 = binary_search_tree.search(60)
if cari1:
    print(f"Ditemukan! Judul: {cari1.judul}.")
else:
    print("Data tidak ditemukan.")

print("[SEARCH] Mancari ID 100...", end=" ")
cari2 = binary_search_tree.search(100)
if cari2:
    print(f"Ditemukan! Judul: {cari2.judul}.")
else:
    print("Data tidak ditemukan.")
print()


print("[STATISTIK] ID Terkecil:", binary_search_tree.get_min())
print("[STATISTIK] ID Terbesar:", binary_search_tree.get_max())
print("[INFO] Tinggi (Height) Tree:", binary_search_tree.height(binary_search_tree.root))
print()

print("=========================================")
print("Simulasi Selesai!")