import random
'''
# data = random.choice([0, 5, 10, 22, 33])
data = random.sample([0, 5, 10, 22, 33],3)
print (data)
# 0~1之間的隨機亂數
a = random.random()
b = random.uniform(0.0, 1.0)
print (a)
print (b)

# 常態亂數；平均數100，標準差10，得到資料多數在 90~110 之間
data = random.normalvariate(100, 10)
print(data)
'''
import statistics as stat
data = stat.mean([1,4,5,8,99,100]) # 平均數
print(data)
data = stat.median([1,4,5,8,99,100]) # 中位數
print(data)
data = stat.stdev([1,4,5,8,99,100]) # 標準差，資料的散佈大小
print(data)