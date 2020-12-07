import requests
response=requests.get("https://1251316161.vod2.myqcloud.com/007a649dvodcq1251316161/ca0008575285890807935673436/aIZjORvGn7IA.mp4")
with open('./a.mp4','wb') as f:
    f.write(response.content)