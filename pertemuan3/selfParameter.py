class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def greet(self):
    print('Hello, my name is ' + self.name)
p1 = Person('Emil', 25)
p1.greet()

#Self parameter harus menjadi parameter pertama dari metode mana pun dalam kelas.
#Self parameter juga bisa digunakan untuk mengakses properti apa pun dari kelas tersebut.

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
  def display_info(self):
    print(f'{self.year} {self.brand} {self.model}')
car1 = Car('Toyota', 'Corolla', 2020)
car1.display_info()