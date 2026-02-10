'''
SOAL 1

Diberikan sebuah list angka:
angka = [10, 20, 30, 40, 50]
1. Tambahkan angka 60 ke dalam list.
2. Hapus angka 20 dari list.
3. Tampilkan angka tertinggi dan terendah
4. Hitung rata-rata angka setelah perubahan data
5. Tampilkan seluruh isi list setelah perubahan.
'''

angka = [10, 20, 30, 40, 50]
angka.append(60) #menambahkan angka 60  ke dalam list
print(angka)

angka.remove(20) #hapus angka 20 dari list
print(angka)

nilaiMax = max(angka)
nilaiMin = min(angka)
print('Angka tertinggi (max) pada data adalah', max(angka)) #menampilkan angka tertinggi setelah perubahan data
print('Angka terkecil (min) pada data adalah', min(angka)) #menampilkan angka terendah setelah perubahan data

jumlah = 0
for x in angka:
    print(x)
    jumlah = jumlah + x
rata_rata = jumlah / 5 #menghitung rata-rata angka setelah perubahan data
print(rata_rata)

print(angka) #menampilkan seluruh isi list perubahan data


'''
SOAL 2

Diberikan sebuah tuple data mahasiswa:
mahasiswa = ("A001", "Budi", "Informatika")
1. Tampilkan nama mahasiswa dari tuple tersebut.
2. Tampilkan seluruh isi tuple menggunakan perulangan for.
3. Jelaskan satu alasan mengapa tuple tidak bisa diubah.
'''

mahasiswa = ('A001', 'Budi', 'Informatika')
print(mahasiswa[1]) #menampilkan nama mahasiswa dari tuple dimana berada pada indeks ke-1

for x in mahasiswa:
    print(x) #menampilkan seluruh isi tuple menggunakan perulangan for

#tuple tidak dapat diubah karena bersifat unchangeable, tuple juga dirancang untuk menyimpan kumpulan data yang bersifat tetap, supaya dapat menjaga keamanan data dan memori


'''
SOAL 3

Diberikan dua set mata kuliah pilihan:
kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}
1. Tentukan mata kuliah yang diambil oleh kedua kelas.
2. Tentukan mata kuliah yang hanya diambil kelas A.
3. Tentukan seluruh mata kuliah unik yang diambil oleh kelas A dan B.
'''

kelas_A = {'Struktur Data', 'Basis Data', 'AI', 'Pemrograman Web'}
kelas_B = {'Struktur Data', 'Machine Learning', 'AI', 'Cloud Computing'}

duaKelas = kelas_A & kelas_B
print(duaKelas) #menampilkan mata kuliah yang diambil kedua kelas

hanyaA = kelas_A - kelas_B
print(hanyaA) #menampilkan mata kuliah yang hanya diambil kelas A

kelasUnik = kelas_A ^ kelas_B
print(kelasUnik) #menampilkan seluruh mata kuliah unik yang diambil oleh kelas A dan B


'''
SOAL 4

Sebuah data mahasiswa disimpan dalam bentuk dictionary:
mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}
1. Tampilkan nama mahasiswa yang memiliki IPK di atas 3.5.
2. Hitung rata-rata IPK seluruh mahasiswa.
3. Tambahkan satu data mahasiswa baru ke dalam dictionary tersebut.
'''

mahasiswa = {
    "A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
    "A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
    "A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}

for nim, data in mahasiswa.items():
    if data["ipk"] > 3.5:
        print(f"Mahasiswa dengan IPK di atas 3.5: {data['nama']}")


total_ipk = sum(data["ipk"] for data in mahasiswa.values())
rata_rata = total_ipk / len(mahasiswa)

print(f"Rata-rata IPK: {rata_rata:.2f}")


mahasiswa["A004"] = {"nama": "Dafa", "prodi": "Teknik Informatika", "ipk": 3.96}