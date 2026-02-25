'''
Buatlah sebuah class dengan
- minimal 3 atribut / property
- 2 method

Lalu buatlah 3 object dari class tersebut
Lalu ubahlah salah satu atribut dari object tersebut
'''

class Bunga:
    def __init__ (self, nama, warna, ukuran):
        self.nama = nama
        self.warna = warna
        self.ukuran = ukuran

    def print_nama(self):
        print(self.nama)

    def klasifikasi(self):
        print(self.nama, 'memiliki warna', self.warna, 'dan ukuran', self.ukuran)

    def ubah_nama(self, namaBaru):
        self.nama = namaBaru

bunga1 = Bunga('Matahari', 'Kuning', 'Besar')
bunga2 = Bunga('Mawar', 'Merah', 'Sedang')
bunga3 = Bunga('Melati', 'Putih', 'Kecil')

bunga1.print_nama()
bunga2.klasifikasi()

bunga3.ubah_nama('Tulip')
print(bunga3.nama)