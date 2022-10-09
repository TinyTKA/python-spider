import json
import time

import requests
import bs4


# url = "https://api.bilibili.com/x/relation/followings?vmid=28249424&pn=2&ps=20&order=desc&order_type=attention
# &jsonp=jsonp"
# 拼接url，返回url字符串
def FormUrl(uid, page):
    return "https://api.bilibili.com/x/relation/followings?vmid=" + uid + "&pn=" + str(
        page) + "&ps=20&order=desc&order_type=attention&jsonp=jsonp"


# 请求头，模拟实际浏览器访问
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37"
}
# 获取uid输入
uid = input("请输入UID")

# 请求分页，每页20项。最多查询前五页
for i in range(1, 5):
    url = FormUrl(uid, i)
    # 延时1秒，防止请求过快被反爬
    time.sleep(1)
    # 发送get请求，获取返回的json字符串
    req = requests.get(url=url, headers=headers)
    # 解析json字符串，返回一个字典
    dicts = json.loads(req.text)
    # 获取字典的“data”“list”段，是一个列表
    lists = dicts["data"]['list']
    # print(type(lists))
    # 循环输出列表内的信息
    for i in lists:
        print(i["uname"] + "\n")
