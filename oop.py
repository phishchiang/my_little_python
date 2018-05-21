class Employee:

  raise_amount = 1.04
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + '.' + last + '@email.com'
    self.pay = pay
  
  def fullname(self):
    return f'{self.first}{self.last}'
  
  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay) # Let these variable inherit from parent class
    self.prog_lang = prog_lang

class Manager(Employee):
  def __init__(self, first, last, pay, employees = None): # Never pass mutable data typs like a list or dic as default arguments; so assing None
    super().__init__(first, last, pay)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees

  def add_emp(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)

  def sub_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)
  
  def print_emps(self):
    for emp in self.employees:
      print (emp.fullname())



emp_01 = Employee('Phish', 'Chiang', 25000)
emp_02 = Employee('Jake', 'BBB', 33000)
dev_01 = Developer('hank', 'CCC', 50000, 'python')
mng_01 = Manager('Joe', 'DDD', 75000 , [dev_01]) 


print (emp_01.pay)
print (dev_01.prog_lang)

emp_01.apply_raise()
print (emp_01.pay)


mng_01.print_emps()
mng_01.add_emp(emp_01)
mng_01.add_emp(emp_02)
mng_01.print_emps()
