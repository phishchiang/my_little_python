import os, fnmatch

os.chdir('D:\\python\\pythonFun\\fileTestFolder')
# print("\")
# print(os.getcwd())

for f in os.listdir():
  print (f)
  if fnmatch.fnmatch(f, '*.txt'):
    
    
    f_name, f_format = os.path.splitext(f)
    f_title, f_course, f_number = f_name.split('-')
    # Strip away any white space on the left and right
    f_title = f_title.strip()
    f_course = f_course.strip()
    # [:] remove specific chracter; .zfill 給定數字的位數
    f_number = f_number.strip()[1:].zfill(2)

    # print('{}-{}-{}{}'.format(f_number, f_course, f_title, f_format))
    new_name = '{}-{}-{}{}'.format(f_number, f_course, f_title, f_format)
    print (new_name)
    # os.rename(f, new_name)
    