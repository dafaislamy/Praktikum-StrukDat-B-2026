pasien_hari_ini = [
{"id": "P001", "nama": "Andi ", "usia": 34, "penyakit": "Flu  ", "bayar": False},
{"id": "P002", "nama": "Budi ", "usia": 22, "penyakit": "Tifus", "bayar": True},
{"id": "P003", "nama": "Cici ", "usia": 45, "penyakit": "Flu  ", "bayar": False},
{"id": "P004", "nama": "Dani ", "usia": 30, "penyakit": "Maag ", "bayar": True},
{"id": "P005", "nama": "Eva  ", "usia": 28, "penyakit": "Tifus", "bayar": False},
{"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag ", "bayar": False},
]

def tampilkan_pasien():
    print("===== DATA PASIEN KLINIK =====")
    print("No | ID   | Nama  | Usia | Penyakit | Status Bayar")
    print("---+------+-------+------+----------+-------------")
    for i in range(len(pasien_hari_ini)):
        print(f"{i+1}  | {pasien_hari_ini[i]["id"]} | {pasien_hari_ini[i]["nama"]} | {pasien_hari_ini[i]["usia"]}   | {pasien_hari_ini[i]["penyakit"]}    | {pasien_hari_ini[i]["bayar"]}")

def filter_belum_bayar():
    print("===== PASIEN BELUM BAYAR =====")

    belum_bayar = [x for x in range(len(pasien_hari_ini)) if pasien_hari_ini[x]["bayar"] == False]
    total = 0

    for i in belum_bayar:
        print(f"{total+1}. {pasien_hari_ini[i]["nama"]}")
        total += 1

    print(f"Total belum bayar: {total}")

tampilkan_pasien()
filter_belum_bayar()


def info_klinik(info):
    print("Info Klinik:")
    print(f"Nama : {info[0]}")
    print(f"Alamat : {info[1]}")
    print(f"Telp : {info[2]}")


def rekap_penyakit():
    penyakit_unik = {}
    jumlah_penyakit = 0

    for i in range(pasien_hari_ini):
        pass


print("")
print("Info Klinik:")
print("Nama   : Klinik Sehat Bersama")
print("Alamat : Jl. Merdeka No. 10, Pekanbaru")
print("Telp   : 0761-12345")
print("")
print("Jenis Penyakit Unik: {'Flu', 'Tifus', 'Maag'}")
print("Jumlah jenis penyakit: 3")
print("")
print("Rekap per penyakit:")
print("Flu   : 2 pasien")
print("Tifus : 2 pasien")
print("Maag  : 2 pasien")
print("")
print("Penyakit terbanyak: Flu, Tifus, Maag (2 pasien)")
print("")



class Pasien:
    def __init__(self):
        self.__id = ""
        self.__nama = ""
        self.__penyakit = ""

    def tampilkan_info():
        pass

    def hitung_pasien():
        pass


class PasienPrioritas:
    pass


print("ID       : P001")
print("Nama     : Andi")
print("Penyakit : Flu")
print("")
print("ID         : P007")
print("Nama       : Ghani")
print("Penyakit   : Sesak Napa")
print("Prioritas  : Darurat")
print("** Segera tangani! **")
print("Total pasien terdaftar: 2")
print("")



class Node:
    pass
    
class AntrianPasien:
    def tambah(data):
        pass

    def tampilkan():
        pass

    def panggil_berikutnya():
        pass

    def cari(nama):
        pass

    def hapus_berdasarkan_id(id):
        pass

    def hitung():
        pass


print("===== ANTRIAN PASIEN =====")
print("[1] P001 - Andi  | Flu")
print("[2] P002 - Budi  | Tifus")
print("[3] P003 - Cici  | Flu")
print("[4] P004 - Dani  | Maag")
print("Total antrian: 4")
print("")
print("Memanggil pasien berikutnya...")
print("Silakan masuk: Andi (P001) - Flu")
print("")
print("===== ANTRIAN PASIEN =====")
print("[1] P002 - Budi  | Tifus")
print("[2] P003 - Cici  | Flu")
print("[3] P004 - Dani  | Maag")
print("Total antrian: 3")
print("")
print("Menghapus pasien dengan ID P003...")
print("Cici (P003) berhasil dihapus dari antrian.")
print("")
print("===== ANTRIAN PASIEN =====")
print("[1] P002 - Budi  | Tifus")
print("[2] P004 - Dani  | Maag")
print("Total antrian: 2")
print("")
print("Mencari 'Dani'...")
print("Ditemukan: P004 - Dani | Maag (posisi ke-2)")
print("")
print("Total antrian: 2")