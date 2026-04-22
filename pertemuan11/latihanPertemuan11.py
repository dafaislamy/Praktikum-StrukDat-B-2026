class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.head is None
    
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1
        print(f"Antrian {self.count}: {nama} - {keluhan}")

    def dequeue(self):
        if self.is_empty():
            return "Queue kosong: Tidak ada antrian untuk dihapus."
        
        temp_data = self.head.nama
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.count -= 1
        return temp_data
    
    def peek(self):
        if self.is_empty():
            return "Queue kosong"
        return self.head.nama
    
    def size(self):
        return self.count
    
    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0
        return self.count
    

print("====================================")
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("====================================")

antrian_pasien = QueueLinkedList()

cek_antrian = antrian_pasien.is_empty()
print(f"Apakah antrian kosong?: {cek_antrian}\n")

antrian_pasien.enqueue("Budi", "Demam Tinggi")
antrian_pasien.enqueue("Ani", "Batuk Pilek")
antrian_pasien.enqueue("Citra", "Sakit Kepala\n")

jumlah_antrian = antrian_pasien.size()
print(f"Jumlah pasien menunggu: {jumlah_antrian} orang\n")

pasien_berikutnya = antrian_pasien.peek()
print(f"Pasien berikutnya: {pasien_berikutnya}\n")

panggil_pasien = antrian_pasien.dequeue()
print(f"Dokter memanggil: {panggil_pasien}\n")

antrian_pasien.enqueue("Dodi", "Nyeri Perut\n")

panggil_pasien = antrian_pasien.dequeue()
print(f"Dokter memanggil: {panggil_pasien}\n")

jumlah_antrian = antrian_pasien.size()
print(f"Jumlah pasien menunggu: {jumlah_antrian} orang\n")

kosongkan_antrian = antrian_pasien.clear()
print(f"Sesi poliklinik selesai. Antrian dikosongkan")
print(f"Jumlah pasien menunggu: {kosongkan_antrian} orang\n")

print("====================================")
print("Simulasi Selesai!")
print("====================================")