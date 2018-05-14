
# 找出整數平方根
n = input('請輸入一個數字')
n = int(n)

for i in range(n):
  # print (i)
  if i * i ==n:
    print ('有正整數開根', i)
    break # 用 break 強制結束迴圈時，不會執行 else 區塊
else:
  print ('沒有正整數開根')

'''
sum = 0
for n in range(11):
  sum += n
print (sum)
'''