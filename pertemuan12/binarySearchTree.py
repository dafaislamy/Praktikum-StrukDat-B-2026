class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        #Langkah 1 : Buat node baru (new)
        new = Node(data)
        
        #Langkah 2 : Cek apakah root = None, jika ya, root = new, selesai, jika tidak lanjut ke langkah 3
        if self.root == None:
            self.root = new
            return
        
        #Langkah 3 : Tentukan P = root, Q = root
        P = self.root
        Q = self.root

        #Langkah 4 : Kerjakan langkah 5 dan 6 selama Q != None dan new.info != P.info
        while Q != None and new.data != P.data:
            #langkah 5 : Tentukan P = Q
            P = Q

            #Langkah 6 : Jika new.info < P.info, maka Q = P.kiri, Jika tidak, maka Q = P.kanan
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right

        #Langkah 7 : Cek apakah new.info = P.info, Jika ya, tampilkan pesan duplikat, selesai, Jika tidak, lanjut ke langkah 8
        if new.data == P.data:
            print("Data Duplikat")
            return
        
        #Langkah 8 : Jika new.info < P.info, maka P.kiri = new, Jika tidak, maka P.kanan = new
        if new.data < P.data:
            P.left = new
        else:
            P.right = new

        #Langkah 9 : Selesai

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=" ")
        in_order(node.right)

bst = BinarySearchTree()

bst.insert(16)
bst.insert(27)
bst.insert(6)
bst.insert(70)
bst.insert(61)

in_order(bst.root)