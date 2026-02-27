# Module math
import math
print(math.pi) # 3.14159...
print(math.sqrt(16)) # 4.0
print(math.ceil(4.3)) # 5


# Module random
import random
print(random.randint(1, 10)) # angka acak 1-10
print(random.choice(['A','B','C'])) # pilih acak dari
list

# Module datetime
from datetime import datetime, date
sekarang = datetime.now()
print(sekarang.strftime('%d-%m-%Y %H:%M'))

# Module os
import os
print(os.getcwd()) # direktori saat ini
print(os.listdir('.')) # daftar file di folder


# Import seluruh module
import math
math.sqrt(9) # harus pakai prefix 'math.'

# Import fungsi tertentu saja
from math import sqrt, pi
sqrt(9) # langsung pakai tanpa prefix

# Import dengan alias (nama pendek)
import datetime as dt
import random as rnd

# Import semua (tidak disarankan)
from math import * # import semua, bisa konflik nama