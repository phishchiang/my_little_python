#  Import Package
import my_package.point
result = my_package.point.distance(3,4)
print (f'距離為 {result}')

import my_package.line as line
result = line.len(1,1,3,3)
print (f'線段長度 {result}')

result = my_package.line.slope(1,1,3,3)
print (f'斜率為 {result}')