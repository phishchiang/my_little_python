'''
# 網路連線
import urllib.request as request
src ='http://www.ntu.edu.tw/'
with request.urlopen(src) as response:
  data=response.read().decode('utf-8') # 使用utf-8解碼
print(data)
'''
# 串接、擷取公開資料
import urllib.request as request
import json
src ='http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c'
with request.urlopen(src) as response:
  data=json.load(response) # 利用 json 模組處理資料
# print(data)
# 將公司名稱列表出來
clist=data['result']['results'] # print(clist) # 一個列表；看資料的最後只有一個中括號結尾
with open('writeOpenData.txt', 'w', encoding='utf-8') as file:
  for company in clist:
    # file.write(company['公司名稱'])
    file.write(company['公司名稱']+'\n')
    

