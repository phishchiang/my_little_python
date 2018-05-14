'''
# For Loops
list1 = ["Apple", "Bananas", "Cherries"]
for i in list1:
  print (i)
# range( start, end, increment )
for i in range(0,10,2):
  print (i)

for i in range (0,51,5):
  print(i)
  i = i*i
print(i)
'''
'''
# While Loops (when you don't know how many times of iterate)
c = 0
while c<5:
  print (c)
  if c == 3:
    break
  c += 1
  '''
'''
# continue will skip the command
c = 0
while c<5:
  c += 1
  if c == 3:
    continue
  print(c)
'''
'''
try:
  if name >3:
    print("The script works")
except:
  print("There's something wrong with your code!")
'''


'''
sum = 0
for x in range(1, 11):
    sum = sum + x
print (sum)

for y in [3, 5, 7, 12256]:
    print (y)


list1 = ['1', '2', '3']
name, age, height = list1
print (height)
print (list1[0])
'''

names = ['Alice', 'Bob', 'Cindy']
for index, element in enumerate(names):
  print ('{},{}'.format(index, element))