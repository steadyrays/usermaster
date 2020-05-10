import re
import requests
# 下载一张图片
# pic_url="https://img9.bcyimg.com/drawer/136527/post/c0jdy/81d890cc23d2481b989dc823eb4dfb49.png"
# response=requests.get(pic_url)
# with open(r"D:\pycharm\pycharm_dm\python练习\图片练习\壁纸3.png",'wb')as f:
#     f.write(response.content)

# count=1
# for i in range(6):
#     # 访问url获得html文本,从html文本中解析出所有的图片链接
#     start_url='https://tieba.baidu.com/p/5815297430?pn=%s'%(i+1)
#     response=requests.get(start_url)
#     html=response.content.decode('utf-8')
#     # print(html)
#     # """src="https://imgsa.baidu.com/forum/w%3D580/sign=7d1327ee2d3fb80e0cd161df06d32ffb/5acb00e93901213fc4f4650358e736d12d2e9501.jpg"""
#     pattern=re.compile('src="(https://imgsa.baidu.com/forum.*?.jpg)"')
#     # 获得所有图片链接
#     url_list=re.findall(pattern,html)
#     # 依次下载所有图片
#     for url in url_list:
#         response=requests.get(url)
#         with open(r"E:\class06_python\百度贴吧图片\美图%s.jpg"%count,'wb')as f:
#             f.write(response.content)
#             print("当前正在下载第%s张图片..........."%count)
#         count+=1

# 1、请求初始url获得html文本
# 2、解析html文本获取需要访问的url
# 3、请求url并且下载到本地

# import re
# import requests
#
# #请求网页获取url
# def get_html(url):
#     header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
#     response=requests.get(url,headers=header)
#     return response.content.decode('gbk')
#
# #解析网页,获取网页信息
# def parse_html(html):
#     pattern=re.compile('src="(/uploads/allimg.*?.jpg)"')
#     url_list=re.findall(pattern,html)
#     print(url_list)
#     return url_list
#
# #下载图片
# def save_picture(url,count):
#     response=requests.get(url)
#     with open(r"D:\pycharm\pycharm_dm\python练习\图片练习\壁纸%s.jpg"%count,'wb')as f:
#         f.write(response.content)
#         print("正在下载第%s张图片....." % count)
#
# #主函数
# def main():
#     count=1
#     for i in range(3):
#         start_url='http://pic.netbian.com/index_%s.html'%(i+1)
#         html=get_html(start_url)
#         url_list=parse_html(html)
#         for url in url_list:
#             save_picture(url,count)
#             count+=1
# main()


















