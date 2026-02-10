#sub-bab 'python dictionaries'

'''
dictionary berguna untuk menyimpan data berdasarkan key dan value
dictionary bersifat ordered, changeable dan not allow duplicate
dictionary dideklarasikan menggunakan tanda {} dan menggunakan key dan value
'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#value dari dictionary dapat dipanggil dengan menggunakan key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#dictionary bersifat not allow duplicate sehingga hanya akan ada satu key dengan satu value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict)) #fungsi len berguna untuk mengetahui panjang dari dictionary

#dictionary dapat berisi berbagai tipe data

#fungsi type berguna untuk mengetahui tipe data dari dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#gunakan dict() untuk membuat dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#sub-bab 'access items'

#item didalam dictionary dapat diakses dengan menggunakan key name didalam []
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

x = thisdict.get("model") #juga dapat menggunakan fungsi .get()
print(x)

x = thisdict.keys() #fungsi .keys() akan mengembalikan seluruh key didalam dictionary
print(x)

#menambahkan item baru ke dalam dictionary juga akan menambah key baru kedalamnya
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #sebelum perubahan
car["color"] = "white"
print(x) #setelah perubahan

#fungsi .values() akan mengembalikan seluruh value didalam dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)

#fungsi .items() akan mengembalikan seluruh item didalam dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)


#sub-bab 'change items'

#value dictionary dapat diubah
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#value juga dapat diganti dengan menggunakan fungsi .update
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


#sub-bab 'add items'

#item dictionary dapat ditambah dengan menambah key indeks dan assign value nya
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#item juga dapat ditambah menggunakan fungsi .update
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


#sub-bab 'remove items'

#item dalam dictionary dapat dihapus dengan menggunakan fungsi .pop
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#fungsi .popitem akan menghapus item paling akhir dari dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#item dalam dictionary juga dapat dihapus menggunakan fungsi del
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#fungsi del juga dapat digunakan untuk menghapus keseluruhan dictionary

#fungsi .clear akan menghapus seluruh item didalam dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


#sub-bab 'loop dictionaries'

#loop pada dictionary dapat dilakukan dengan perulangan for
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x]) #akan menampilkan seluruh value dari dictionary

for x in thisdict.values():
  print(x) #juga dapat menggunakan fungsi .values untuk menampilkan seluruh value dictionary

for x in thisdict.keys():
  print(x) #fungsi .keys akan menampilkan seluruh key dari dictionary

for x, y in thisdict.items():
  print(x, y) #untuk menampilkan key dan value dari dictionary, dapat menggunakan fungsi .items


#sub-bab 'copy dictionaries'

#dictionary dapat disalin (copy) ke dictionary baru dengan menggunakan fungsi .copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#juga dapat menggunakan fungsi dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


#sub-bab 'nested dictionaries'

#dictionary dapat diisi dengan dictionary lainnya, dan biasa disebut nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#memasukkan dictionary kedalam dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"]) #cara mengakses value dictionary

#loop dapat dilakukan melalui dictionary dengan menggunakan fungsi .items
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])