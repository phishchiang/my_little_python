'''
# 有順序不可動的列表 Tuple
tuple = (3,4,5)
# 有順序可動的列表 List
list = [3,4,5]
print(list[2])
length = len(list)
print(length)
# 集合 Set
{3,4,5}
'''

'''
# 集合的運算
s3 = {4,5,6}
s4 = {5,6,7}
print (5 in s3)
s5 = s3 & s4 # 交集
s6 = s3 | s4 # 聯集
s7 = s3 - s4 # 差集
print(s5)
print(s6)
print(s7)
'''
'''
# 字典 Dictionary: Key-value
dic = {"apple":"蘋果","data":"資料"}
print(dic["apple"])
print("apple" in dic)
print("蘋果" in dic) # 只有判斷Key，而不是值
del dic["data"] # 刪除字典中的鍵值對
print (dic)
'''
'''
# 字串運算 用\去escape""
s1="Hell\"o"
s2="Hell\\o"
print(s1 +"\r\n"+s2 )
print(s2[2])
'''
message = 'hello world'
message = message.replace('world', 'python')
# print(message.find('worlddd'))
print (message)

greeting = 'Hello'
name = 'John'

greetingMsg = '{}, {}. Welcome!!!'.format(greeting, name)
print (greetingMsg)