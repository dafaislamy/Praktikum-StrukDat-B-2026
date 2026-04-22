'''
Bagian A — Double Linked List

Sistem daftar buku toko "Literasi"
Toko buku "Literasi" ingin mencatat daftar buku (judul & pengarang)
menggunakan Double Linked List agar bisa ditelusuri dari depan maupun belakang.
1. Buat class Node dengan atribut judul, pengarang, prev, dan next.
2. Buat fungsi insert_tail(), lalu tambahkan buku: Laskar Pelangi, Bumi Manusia,
dan Sang Pemimpi.
3. Buat fungsi print_forward() dan print_backward(), lalu jalankan keduanya.
4. Buat fungsi delete_by_judul(), hapus buku "Bumi Manusia", lalu tampilkan list
kembali.
'''

print("\nBagian A - Double Linked List\n")


class NodeDouble:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, judul, pengarang):
        new_node = NodeDouble(judul, pengarang)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        new_node.prev = curr

    def print_forward(self):
        print("Daftar Buku (Forward):")
        curr = self.head
        while curr:
            print(f"- {curr.judul} ({curr.pengarang})")
            curr = curr.next

    def print_backward(self):
        print("Daftar Buku (Backward):")
        curr = self.head
        if not curr: return
        while curr.next:
            curr = curr.next
        while curr:
            print(f"- {curr.judul} ({curr.pengarang})")
            curr = curr.prev

    def delete_by_judul(self, judul):
        curr = self.head
        while curr:
            if curr.judul == judul:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                
                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next

dll = DoubleLinkedList()
dll.insert_tail("Laskar Pelangi", "Andrea Hirata")
dll.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
dll.insert_tail("Sang Pemimpi", "Andrea Hirata")

dll.print_forward()
dll.print_backward()

print("\n--- Menghapus 'Bumi Manusia' ---")
dll.delete_by_judul("Bumi Manusia")
dll.print_forward()

print("")

'''
Bagian B — Circular Linked List

Sistem antrian kasir toko "Literasi"
Kasir toko menggunakan Circular Linked List untuk antrian pelanggan. Antrian
awal: Andi → Budi → Citra → Dina → (kembali ke Andi).
1. Buat class Node dengan atribut nama dan next. Buat fungsi insert_tail() dan
tambahkan 4 pelanggan.
2. Buat fungsi print_antrian() untuk menampilkan satu putaran antrian.
3. Tambahkan pelanggan baru Edo di akhir antrian menggunakan insert_tail(), lalu
tampilkan antrian.
4. Buat fungsi delete_head(), hapus Andi (sudah dilayani), lalu tampilkan antrian.
'''

print("\nBagian B - Circular Linked List\n")


class NodeCircular:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        new_node = NodeCircular(nama)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        
        curr.next = new_node
        new_node.next = self.head

    def print_antrian(self):
        if not self.head:
            print("Antrian Kosong")
            return
        
        res = []
        curr = self.head
        while True:
            res.append(curr.nama)
            curr = curr.next
            if curr == self.head:
                break
        print(" -> ".join(res) + " -> (kembali ke " + self.head.nama + ")")

    def delete_head(self):
        if not self.head: return
        if self.head.next == self.head:
            self.head = None
            return
        
        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        self.head = self.head.next
        curr.next = self.head

cll = CircularLinkedList()
for nama in ["Andi", "Budi", "Citra", "Dina"]:
    cll.insert_tail(nama)

print("Antrian Awal:")
cll.print_antrian()

print("\nMenambahkan Edo:")
cll.insert_tail("Edo")
cll.print_antrian()

print("\nAndi Selesai Dilayani (Delete Head):")
cll.delete_head()
cll.print_antrian()