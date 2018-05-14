dic01 = {'name':'John', 'phone':'0933980284', 'height':'170cm', 'age':'15', 'course': ['Math', 'History']}
dic01['gender'] = 'Female'
print(dic01.get('ddd', 'Not Found'))
age = dic01.pop('age') 
print(age)
print (dic01.items())

for key, value in dic01.items():
  print (key, value)