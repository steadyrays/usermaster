import requests
from lxml import etree
def get_html(url):
    header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    try:
        response=requests.get(url,headers=header)
        # 判断网页是否正确返回
        if response.status_code==200:
            return response.content.decode('utf-8')
        else:
            print("{0}网页请求状态码错误!{0}".format("-"*30))
    except Exception as e:
        print("{0}请求参数出现错误:{1}{0}".format("-"*30,e))

def parse_html(html):
    # 通过xpath提取
    html=etree.HTML(html)
    index=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/i/text()')
    title=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a/text()')
    actor=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/div/div/div[1]/p[2]/text()')
    releasetime=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/div/div/div[1]/p[3]/text()')
    score1=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/div/div/div[2]/p/i[1]/text()')
    score2=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/div/div/div[2]/p/i[2]/text()')
    print(index,title,actor,releasetime,score1,score2)
    # tlist=[]
    # for i in range(len(index)):
    #     tlist.append([index[i],title[i],
    #                   actor[i].strip().replace(",","、").strip("主演："),releasetime[i].strip("上映时间：")
    #                      ,score1[i]+score2[i]])
    # for line in tlist:
    #     print(line)
    # return tlist
def save_to_csv(tlist):
    with open("猫眼电影Top100.csv",'a',encoding='utf-8-sig')as f:
       for line in tlist:
           for word in line:
               f.write(word+',')
           f.write('\n')


def main():
    # 清空文本
    # with open("猫眼电影Top100.csv",'w',encoding='utf-8-sig')as f:
    #     f.write('排名,电影名称,主演,上映时间,评分,\n')
    for i in range(10):
        start_url='https://maoyan.com/board/4?offset=%s'%(i*10)
        html=get_html(start_url)
        parse_html(html)
        # save_to_csv(info)
        # print("正在写入第%s页信息..."%(i+1))

if __name__ == '__main__':
    main()# 调用主函数

print('__name__的值为:',__name__)# 当在自己的模块环境中运行时返回__main__










