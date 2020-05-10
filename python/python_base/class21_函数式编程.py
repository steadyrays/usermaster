# 1、请求初始url获得html文本
# 2、解析html文本获取需要访问的url
# 3、请求url并且下载到本地
import re
import requests
# 请求网页获取url
def get_html(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    response=requests.get(url,headers=header)
    return response.content.decode('utf-8')# 返回html网页文本信息

# 解析网页,获取网页信息
def parse_html(html):
    pattern=re.compile('src="(https://imgsa.baidu.com/forum.*?.jpg)"')
    # 获得所有图片链接
    url_list=re.findall(pattern,html)
    return url_list

# 下载图片
def save_picture(url,count):
    response=requests.get(url)
    with open(r"E:\class06_python\百度贴吧图片\美图%s.jpg"%count,'wb')as f:
        f.write(response.content)
        print("正在下载第%s张图片....."%count)

# 主函数
def main():
    count=1
    print("百度贴吧图片下载")
    for i in range(6):
        start_url='https://tieba.baidu.com/p/5815297430?pn=%s'%(i+1)
        html=get_html(start_url)
        url_list=parse_html(html)
        for url in url_list:
            save_picture(url,count)# 图片下载
            count+=1
main()



