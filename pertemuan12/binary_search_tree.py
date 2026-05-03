class Node: #deklarasi class Node dengan isi id_buku, judul, left, dan right
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree: #deklarasi class BinarySearchTree
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul): #deklarasi fungsi insert untuk memasukkan data kedalam tree dengan syarat jika data lebih kecil dari root, maka diletak disebelah kiri root, jika data lebih besar dari root, maka diletak disebelah kenan root
        new_node = Node(id_buku, judul) #deklarasi variabel new_node untuk membuat sebuah node baru
        if self.root is None: #jika root kosong, maka baris dibawah tidak dijalankan
            self.root = new_node #jika root berisi, maka root diisi new_node
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return
        
        current = self.root #deklarasi variabel current dan diisi root
        while True:
            if id_buku < current.id_buku: #jika id_buku lebih kecil dari id_buku saat ini, maka baris kode dijalankan
                if current.left is None: #jika current.left = None atau masih kosong, maka
                    current.left = new_node #current.left diisi new_node
                    break
                current = current.left #jika current.left sudah ada isinya, maka current = current.left

            if id_buku > current.id_buku: #jika id_buku lebih besar dari id_buku saat ini, maka baris kode dijalankan
                if current.right is None: #jika current.right = None atau masih kosong, maka
                    current.right = new_node #current.right diisi new_node
                    break
                current = current.right #jika current.right sudah ada isinya, maka current = current.right

        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    def search(self, id_buku): #deklarasi fungsi search untuk mencari suatu data didalam tree
        current = self.root #deklarasi variabel current dan diisi root
        while current is not None: #selama current tidak kosong, jalankan baris kode 
            if id_buku == current.id_buku: #jika id_buku sama dengan id_buku saat ini
                return current #maka kembalikan current
            elif id_buku < current.id_buku: #jika id_buku lebih kecil dari id_buku saat ini
                current = current.left #maka current = current.left
            else: #jika tidak memenuhi keduanya yaitu id_buku lebih besar dari id_buku saat ini
                current = current.right #maka current = current.right
        return None #jika current = None atau kosong, kembalikan None

    def traversal_inorder(self, node): #deklarasi fungsi traversal_inorder untuk mengurutkan data mulai dari left - root - right yang mana akan menampilkan data yang tersusun dari terkecil ke terbesar
        if node:
            self.traversal_inorder(node.left)
            print(f"{node.id_buku} - {node.judul}")
            self.traversal_inorder(node.right)

    def get_min(self): #deklarasi fungsi get_min untuk mencari id_buku terkecil dari tree
        if self.root is None: #jika root masih kosong
            return None #maka kembalikan None
        current = self.root #deklarasi variabel current dan diisi root
        while current.left: #selama masih ada current.left
            current = current.left #maka current diisi current.left
        return current.id_buku #jika sudah sampai pada ujung tree atau leaf, maka sudah sampai pada tujuan dimana data merupakan data terkecil didalam tree, maka kembalikan id_buku nya

    def get_max(self): #deklarasi fungsi get_max untuk mencari id_buku terbesar dari tree
        if self.root is None: #jika root masih kosong
            return None #maka kembalikan None
        current = self.root #deklarasi variabel current dan diisi root
        while current.right: #selama masih ada current.right
            current = current.right #maka current diisi current.right
        return current.id_buku #jika sudah sampai pada ujung tree atau leaf, maka sudah sampai pada tujuan dimana data merupakan data terbesar didalam tree, maka kembalikan id_buku nya

    def height(self, node): #deklarasi fungsi height untuk menghitung tinggi (level) dari tree
        if node is None: #jika node masih kosong
            return -1 #kembalikan -1, karena tree masih kosong sehingga belum ada level
        left_height = self.height(node.left) #left_height melakukan rekursi dengan memanggil fungsinya kembali yang berfungi untuk sampai pada ujung tree atau leaf disebelah kiri
        right_height = self.height(node.right) #right_height melakukan rekursi dengan memanggil fungsinya kembali yang berfungsi untuk sampai pada ujung tree atau leaf disebelah kanan
        return max(left_height, right_height) + 1 #fungsi mengembalikan ukuran terbesar (max) dari left_height dan right_height kemudian ditambah 1 agar perhitungan tetap bertambah


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