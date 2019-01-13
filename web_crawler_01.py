# 抓取網頁上 HTML 原始碼
import urllib.request as req
# url="https://www.ptt.cc/bbs/movie/index.html"
url="https://www.ptt.cc/bbs/movie/M.1547374454.A.613.html"
# 建立一個 Request 物件，附加 Request Headers 的資訊
request = req.Request(url, headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
})
with req.urlopen(request) as response: # 直接放 url 會被禁止，所以必須傳入 Request Header 偽裝成一般使用者
  data = response.read().decode("utf-8")

# print(data)

# 解析原始碼，取得每篇文章的標題
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
# 取得網頁標題的字串
# print(root.title.string)
titles=root.find_all("div", class_="title") # 尋找 class="title" 的 div 標籤，要加底線
# print(titles)
'''
for title in titles:
  if title.a != None: # 如果標題包含 a 標籤，也沒有被刪除的話，印出來
    print(title.a.string)
    
'''

pushers=root.find_all("span", class_="f3 push-content")
for pusher in pushers:
  # newPusher = pusher.string.replace(": ", "")
  newPusher = pusher.string.replace(": ", "")
  print(newPusher)
