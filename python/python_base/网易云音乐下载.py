
#保存图片、音乐、视频文件用二进制格式wb
#单首音乐下载
# import requests
# url='http://music.163.com/song/media/outer/url?id=1369798757'
# headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
# response=requests.get(url,headers=headers)
# data=response.content
# with open('芒种.mp3','wb')as f:
#     f.write(data)

#批量下载
import requests
from lxml import etree
url='https://music.163.com//discover/toplist?id=3778678'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response=requests.get(url,headers=headers)
data=response.content.decode('utf-8')
#初始化
html=etree.HTML(data)
#歌曲名
name=html.xpath('//ul[@class="f-hide"]/li/a/text()')
id=html.xpath('//ul[@class="f-hide"]/li/a/@href')
print(id)
# for i in range(200):
#     id_all=id[i].split('=')[1]
#     url_all='http://music.163.com/song/media/outer/url?id={}'.format(id_all)
#     res=requests.get(url_all,headers=headers)
#     datas=res.content
#     with open(r"D:\pycharm\pycharm_dm\a课程资料\网易云音乐\{}.mp3".format(name[i]),'wb') as f:
#         f.write(datas)
#         print('下载<%s>完成'%name[i])











































