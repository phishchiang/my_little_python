'''
x = input("請輸入數字:") # 取得字串形式的使用者輸入
x = int(x) #轉換成整數形式
if x>200:
  print("大於200")
elif x>100:
  print("100~200")
else:
  print("小於100")
'''
'''
n1 = int(input("第一個數字:"))
n2 = int(input("第二個數字:"))
op = input("請輸入運算代號:")

if op == "+":
  print ("運算結果為: " + str(n1 + n2))

elif op == "-":
  print ("運算結果為: " + str(n1 - n2))

elif op == "*":
  print ("運算結果為: " + str(n1 * n2))

elif op == "/":
  print ("運算結果為: " + str(n1 / n2))
else:
  print ("不支援的運算")
'''
'''
if (5>3) & (9>2):
  print("& works!!")
if (5>3) and (9>2):
  print("and works!!")
if (5>3) | (1>2):
  print("| works!!")
if (5>3) or (1>2):
  print("or works!!")
'''