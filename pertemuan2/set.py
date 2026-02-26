#sub-bab 'python sets'

#contoh dekalarasi set dengan menggunakan {}
thisset = {"apple", "banana", "cherry"}
print(thisset)

'''
sets memiliki sifat unordered, unchangeable, dan not allow duplicate
- unordered berarti tidak berurutan, set tidak menggunakan indeks sehingga urutan set akan acak
- unchangeable berarti tidak dapat, tetapi set dapat ditambah maupun dikurang
- not allow duplcate berarti isi set tidak dapat memiliki isi yang sama
'''

#set bersifat not allow duplicate sehingga akan menghapus nilai yang sama pada set
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#nilai True dan 1 dianggap sama didalam set sehingga dianggap duplicate, begitu juga nilai False dan 0
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #fungsi len berguna untuk mengetahui panjang set

set1 = {"abc", 34, True, 40, "male"} #set dapat berisi berbagai tipe data

myset = {"apple", "banana", "cherry"}
print(type(myset)) #fungsi type berguna untuk mengetahui tipe data dari set

thisset = set(("apple", "banana", "cherry")) #gunakan set() untuk membuat set
print(thisset)


#sub-bab 'access set items'

#data didalam set tidak dapat diakses menggunakan indeks atau key,
#tetapi dapat melakukan perulangan for untuk melalui item-item dalam
#himpunan atau data dapat dicari menggunakan fungsi in
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) #output akan menghasilkan nilai True


#sub-bab 'add set items'

#untuk menambah data kedalam set dapat menggunakan fungsi .add
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#set juga dapat dimasukkan kedalam set lainnya menggunakan fungsi .update,
#tidak hanya set yang dapat ditambah, struktur data lainnya juga dapat
#ditambah seperti list, tuple maupun dictionary
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


#sub-bab 'remove set items'

#untuk menghapus item dalam set dapat menggunakan fungsi .remove atau .discard
#perbedaan antara remove dan discard adalah ketika menggunakan remove
#jika item yang dihapus tidak terdapat didalam set maka akan menghasilkan error,
#tetapi ketika menggunakan discard tidak akan error
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#fungsi .pop dapat menghapus item didalam set secara random / acak
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#funsi .clear akan menghapus semua item didalam set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#fungsi del akan menghapus seluruh set
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)


#sub-bab 'loop sets'

#loop pada set dapat dilakukan dengan menggunakan perulangan for
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)


#sub-bab 'join sets'

#fungsi .union akan menggabung dua set menjadi satu set baru
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#fungsi union juga dapat menggunakan operator |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#banyak set juga dapat digabung menggunakan fungsi union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

#menggunakan operator |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

#fungsi union dapat menggabungkan set dengan tipe data lain seperti list dan tuple, tetapi operator tidak bisa

#fungsi .update menggabungkan set satu dengan set lainnya
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#fungsi union dan update akan menghapus item duplicate

#fungsi .intersection hanya menyimpan data yang sama antar tiap set yang digabung
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

#fungsi intersection juga dapat menggunakan operator &
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

#fungsi intersection_update menggabungkan item yang sama antar set satu dengan set lainnya
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#nilai True dan 1 dianggap sama sehingga salah satu akan dihapus, begitu juga nilai False dan 0

#fungsi .difference akan menyimpan seluruh item didalam set yang tidak ada didalam set lainnya
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

#fungsi difference juga dapat menggunakan operator -
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

#fungsi difference_update akan menyimpan nilai pada set yang tidak ada didalam set lainnya
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

#fungsi .symmetric_difference akan menyimpan kedalam set baru semua item yang tidak ada di kedua set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

#fungsi symmetric_difference juga dapat menggunakan operator ^
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

#fungsi symmetric_difference_update akan menyimpan seluruh item yang tidak ada didalam kedua set ke dalam set awal
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)


#sub-bab 'frozenset'

'''
frozenset adalah versi set yang tidak dapat diubah
seperti set, frozenset juga mengandung elemen-elemen unik, bersifat  unordered dan unchangeable
tidak seperti set, item didalam frozenset tidak dapat ditambah maupun dikurang
'''

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))