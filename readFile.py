# testFile = open("helloWorld.py", "w")
# print (testFile)
# testFile.write("\nI\nLove\nYou\n!!!")
'''
testFile = open("helloWorld.py", "a+")
testFile.write("\nI\nLove\nYou\n!!!")

position = testFile.tell()
print (position)
position = testFile.seek(0,0)
# testFile.read()
testFile.close()

with open("helloWorld.py", "r") as file:
  bt = file.read()
  print(bt)
# print(fileIn)
'''

with open('helloWorld.py', 'r') as f :
  size_to_read = 3
  f_contents = f.read(size_to_read)
  while len(f_contents) > 0:
    print (f_contents, end='')
    f_contents = f.read(size_to_read)