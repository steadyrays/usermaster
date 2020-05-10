

# 1、确认分析目标,找到目标数据(查看是否在网页源代码)
# 2、
import re
import requests
def get_html(url):
    response=requests.get(url)
    return response.content.decode('utf-8')

def parse_html(html):
    # pattern=re.compile('<p class="star">\s+(.*?)\s+</p>',re.S)
    # pattern=re.compile('<dd>.*?>(\d+)<.*?title="(.*?)".*?主演：(.*?)\s+</p>'
    #                    '.*?上映时间：(.*?)</p>.*?integer">(.*?)<.*?'
    #                    'fraction">(.*?)<.*?</dd>', re.S)
    pattern=re.compile('<dd>.*?>(\d+)<.*?title="(.*?)".*?主演：(.*?)\s+<.*?'
                       '上映时间：(.*?)<.*?integer">(.*?)<.*?'
                       'fraction">(.*?)<.*?</dd>',re.S)# re.S让点号能匹配换行符
    info=re.findall(pattern,html)
    return info
def save_to_csv(tlist):
    with open("猫眼电影Top100.csv",'a',encoding='utf-8')as f:
        for line in tlist:
            print(line)
            for i in range(len(line)):
                if i==2:
                    f.write(line[i].replace(",","、")+',')
                elif i<4:
                    f.write(line[i]+',')
                else:
                    f.write(line[i]+line[i+1])
                    break
            f.write('\n')

def main():
    # 清空文本
    with open("猫眼电影Top100.csv",'w',encoding='utf-8')as f:
        f.write('')
    for i in range(10):
        start_url='https://maoyan.com/board/4?offset=%s'%(i*10)
        html=get_html(start_url)
        info=parse_html(html)
        save_to_csv(info)
        print("正在写入第%s页信息..."%(i+1))
main()

