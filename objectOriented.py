'''
#  self 像是 this一樣傳入物件本身，
# 類似於 Person.getAge(person) 這樣
class Person:
  def getName(self):
    print ("Avi")
  def getAge(self):
    print ("16")

person = Person()

person.getName()
person.getAge()
'''
'''
# Initialization function : Takes parameters you want to pass in when creating the object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print ("You just created a guy named " + self.name)
  def getName(self):
    print ("Your name is " + self.name)
  def getAge(self):
    print ("Your age is " + self.age)

p1 = Person("Bob", "22")
p1.getName()
p1.getAge()
print (p1.name)
print (p1.age)
'''
# Inheritance
class Parent():
  def __init__(self):
    print ("This is parent class!")
  def parentFunc(self):
    print ("This is parent function!")

class Child(Parent):
  def __init__(self):
    print ("This is child class!")
  def childFunc(self):
    print ("This is child function!")

p = Parent()
p.parentFunc()
c = Child()
c.childFunc()
c.parentFunc()