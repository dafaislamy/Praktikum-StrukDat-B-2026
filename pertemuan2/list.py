#sub-bab 'python list'

thislist = ['Apple', 'Banana', 'Cherry']
print(thislist)

'''
List memiliki sifat ordered yaitu terurut, artinya item-item tersebut
memiliki urutan yang telah ditentukan, dan urutan tersebut tidak akan berubah.
jika item baru ditambahkan ke dalam daftar, item baru tersebut akan ditempatkan
di akhir daftar. List juga memiliki sifat changeable, artinya item dapat diubah,
ditambah, dan dihapus dalam daftar setelah daftar tersebut dibuat.
'''

#isi list dapat memiliki nilai yang sama
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#fungsi len berguna untuk mengetahui panjang list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#list dapat menyimpan berbagai tipe data
list1 = ["abc", 34, True, 40, "male"]

#fungsi type berguna untuk mengetahui tipe data
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#constructor list() berguna ketika ingin membuat list baru
thislist = list(("apple", "banana", "cherry"))
print(thislist)


#sub-bab 'access list items'

#untuk mengakses isi dari list dapat menggunakan indeks yang dimulai dari 0
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#indeks negatif akan menghitung indeks dari belakang list, sehingga output yang akan dihasilkan adalah 'cherry'
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#range indeks berguna ketika ingin menampilkan isi dari list dari indeks ke-n menuju indeks ke-m
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #output : apple, banana, cherry, orange

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #output : cherry, orange, kiwi, melon, mango

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #output : oange, kiwi, melon

#untuk mengecek data apakah ada atau tidak, dengan menggunakan fungsi in
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#sub-bab 'change list items'

#item didalam list dapat diganti dengan menggunakan penunjuk indeks
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#penganntian juga dapat dilakukan sekaligus dengan menggunakan range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#jika item yang ditambah lebih banyak dari yang diganti,
#maka item tersebut akan dimasukkan ketempat spesifik
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#jika item yang ditambah lebih sedikit dari yang diganti,
#maka item yang dimasukkan akan masuk dan item sisa akan dikeluarkan
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#sub-bab 'add list items'

#fungsi .append berguna untuk menambahkan item kedalam list dan akan ditaruh ke indeks paling akhir list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#fungsi .insert berguna untuk menambahkan item kedalam list dengan indeks spesifik
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#jika ingin menambah list kedalam liat lain, dapat menggunakan fungsi .extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#fungsi extend juga dapat menambah tipe lain seperti tuple, set ataupun dictionary


#sub-bab 'remove list items'

#fungsi .remove berguna untuk menghapus item dari list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#jika terdapat lebih dari satu item dengan nama yang sama, maka item yang terhapus hanya item pertama yang ditemukan
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#fungsi .pop berguna untuk menghapus item list menggunakan indeks
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#jika indeks tidak dimasukkan kedalam fungsi pop, maka item yang dihapus akan random

#fungsi del juga dapat menghapus item menggunakan indeks dan dapat menghapus keseluruhan list tersebut
thislist = ["apple", "banana", "cherry"]
del thislist

#fungsi .clear berguna untuk menghapus seluruh isi item dalam list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#sub-bab 'loop lists'

#loop pada list dapat dilakukan dengan menggunakan perulangan for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#loop juga dapat digunakan menggunakan indeks numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): #menggunakan fungsi range dan len
  print(thislist[i])

#loop juga dapat menggunakan perulangan while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#list comprehension dapat memperpendek penulisan for loop
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#sub-bab 'list comprehension'

#kode ingin menampilkan list fruits yang hanya mengandung huruf a didalamnya
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#dengan menggunakan list comprehension, perulangan for dapat disingkat menjadi satu baris
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#syntaxnya : newlist = [expression for item in iterable if condition == True]

#hanya menerima item yang tidak apel
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#dapat menggunakan fungsi range untuk menciptakan iterable
newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5] #menggunakan kondisi
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


#sub-bab 'sort lists'

#list akan diurutkan berdasarkan urutan alfabet
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#list akan diurutkan berdasarkan urutan angka
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#urutan dapat dibalik dengan menggunakan argumen reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#sort function dapat di costumize menggunakan key = function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#huruf besar akan lebih dulu daripada huruf kecil (case insensitive sort)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#tetapi, jika ingin mengurutkan dari kecil ke besar,
#dapat menggunakan funsi bawaan sebagai fungsi utama saat mengurutkan data
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#fungsi .reverse akan membalik urutan dari list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#sub-bab 'copy lists'

#fungsi .copy berguna untuk meng-copy (salin) list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#gunakan list() untuk membuat list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#menyalin list juga dapat menggunakan opearor :
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


#sub-bab 'join lists'

#list dapat digabung menggunakan operator +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#cara lain untuk menambah list satu ke list lainnya adalah dengan menggunakan
#fungsi append dan dilakukan satu per satu menggunakan for loop
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#atau dapat menggunakan fungsi .extend untuk menggabungkan list satu dengan list lainnya
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)