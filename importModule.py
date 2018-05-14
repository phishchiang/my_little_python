import my_module

import sys
# 加入一個相對路徑 modules
sys.path.append("modules")
# courses = ['History', 'Math', 'Physics', 'CompSci']
import helloModule as hm
# print (sys.path)

print (hm.go_fuc('Fish!!'))
