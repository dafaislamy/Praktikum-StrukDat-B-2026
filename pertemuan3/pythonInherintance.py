#Inheritance memungkinkan untuk mendefinisikan
#sebuah kelas yang mewarisi semua metode dan properti dari kelas lain
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student('Mike', 'Olsen')
x.printname()

#python juga memiliki fungsi super()
#yang akan membuat kelas turunan mewarisi semua metode dan properti dari kelas induknya
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)