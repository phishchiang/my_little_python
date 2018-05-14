#Functions
'''

def helloWorld(arg):
  print(arg + " !!!")
helloWorld("Hello World")

def sumFunc(n1, n2):
  print (n1 + n2)
sumFunc(10, 15)
'''
'''
def sumFunc(n1, n2):
  # print (n1 + n2)
  return n1 + n2

sumResult = sumFunc(10, 15)
print (sumResult)
'''
'''
# n1 = abs(-56.562)
# print(n1)

# bool(0)
# Tell all func you can use of specific item
sent1 = "string"
help(sent1.upper)
# Take string as a python code
print (eval("5*3"))

sent2 = "print('Hi')"
eval(sent2)
'''
'''
def helloFunc(greeting, name = 'You'):
  return '{}, {}'.format(greeting, name)
print (helloFunc('Hello', 'Mike'))
'''
def student_info(*args, **kwargs):
  print(args) # Become Tuple
  print(kwargs) # key word arguments : Become Dictionary
course = ['Math', 'Art']
info = {'name': 'Hojn', 'age': 22}
student_info(*course, **info)
# student_info('Math', 'Art', name='Hojn', age=22)