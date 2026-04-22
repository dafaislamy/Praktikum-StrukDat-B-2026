'''
2. Case: Sistem Antrean Pasien (Emergency Room)
Skenario: Di sebuah rumah sakit, pasien datang dengan tingkat urgensi yang berbeda. Secara
default, pasien baru akan mengantre di belakang. Namun, jika ada pasien "Darurat", mereka harus
disisipkan di posisi tertentu (misalnya posisi ke-2) agar segera ditangani setelah pasien pertama
yang sedang diperiksa.
Data Awal (Antrean saat ini): ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

Tugas 1: Implementasi pada List Array
Gunakan list bawaan Python antrean_array.
1. Buat list antrean_array dengan data awal di atas.
2. Buat fungsi sisipkan_pasien_darurat_array(nama_pasien, posisi):
o Gunakan metode .insert(posisi - 1, nama_pasien).
o Analisis: Apa yang terjadi pada pasien di belakangnya saat pasien baru masuk di
tengah?
3. Cetak antrean akhir.

Tugas 2: Implementasi pada Singly LinkedList
Gunakan class Node dan AntreanLinkedList.
1. Implementasikan fungsi insert_at_position(head, nama_pasien, posisi) seperti kode yang
kamu punya sebelumnya (menggunakan logika position - 2).
2. Tugas Tambahan: Tambahkan validasi sederhana. Jika posisi yang dimasukkan lebih besar
dari jumlah pasien yang ada, maka pasien tersebut otomatis diletakkan di paling akhir
(Append).
'''

#Tugas 1
antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    antrean_array.insert(posisi - 1, nama_pasien)
    return antrean_array

antrean_baru = sisipkan_pasien_darurat_array("Pasien D (Darurat)", 2)
print(antrean_baru)

#Tugas 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntreanLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_position(self, nama_pasien, posisi):
        new_node = Node(nama_pasien)
        
        if posisi <= 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 1
        
        while current.next is not None and count < posisi - 1:
            current = current.next
            count += 1
        
        new_node.next = current.next
        current.next = new_node

    def cetak_antrean(self):
        temp = self.head
        hasil = []
        while temp:
            hasil.append(temp.data)
            temp = temp.next
        print("Antrean LinkedList Akhir:", hasil)

antrean_baru = AntreanLinkedList()
antrean_baru.append("Pasien A (Stabil)")
antrean_baru.append("Pasien B (Stabil)")
antrean_baru.append("Pasien C (Stabil)")

antrean_baru.insert_at_position("Pasien X (DARURAT)", 2)

antrean_baru.insert_at_position("Pasien Y (Stabil)", 10)

antrean_baru.cetak_antrean()