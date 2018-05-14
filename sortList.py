
'''
# Run each element thurough this absolute function before it sort
li = [1 ,2 ,-5 ,-9 ,3 ,-4 ]
s_li = sorted(li, key = abs)

print (s_li)
'''
# Sorting the Object
class Employee ():
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

  def __repr__(self):
    return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Zach', 55, 32000)
e2 = Employee('Mary', 24, 25000)
e3 = Employee('Susan', 30, 30000)
e4 = Employee('Tom', 45, 50000)


employees = [e1, e2, e3, e4]

def sortEmp(self):
  return self.salary

s_employees = sorted(employees, key=sortEmp, reverse=True)
# Anonymous function
# s_employees = sorted(employees, key=lambda e:e.salary, reverse=True)
print (s_employees)
