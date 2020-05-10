'http://www.7799520.com/api/user/pc/list/search?marry=3&page=2'
import requests
import json
from multiprocessing import Pool# 进程池
import time,random
# 获取网页源代码
def get_html(url):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    try:
        response = requests.get(url, headers=header)
        # 判断网页是否正确返回
        if response.status_code == 200:
            return response.content.decode('gbk')
        else:
            print("{0}网页请求状态码错误!{0}".format("-" * 10))
    except Exception as e:
        print("{0}请求参数出现错误:{1}{0}".format("-" * 10, e))

def parse_html(html):
    info=json.loads(html)['data']['list']
    tlist=[]
    for line in info:
        # print(line)
        userid=line['userid']
        province=line['province']
        city=line['city']
        height=line['height']
        education=line['education']
        username=line['username'].replace("\n"," ")
        monolog=line['monolog'].replace("\n"," ")
        year=line['birthdayyear']
        gender=line['gender']# 1男性 2女性
        salary=line['salary']
        marry=line['marry']
        tlist.append([userid,username,gender,year,education,province,city,height,salary,marry,monolog])
    # for line in tlist:
    #     print(line)
    #     print("- - "*20)
    return tlist
def save_to_csv(tlist):
    with open('我主良缘婚姻介绍.csv','a',encoding='utf-8-sig')as f:
        for line in tlist:
            for word in line:
                f.write(word+',')
            f.write('\n')

def main(i):
    start_url='http://www.7799520.com/api/user/pc/list/search?marry=1&page={}'.format(i)
    page=get_html(start_url)
    print("正在访问第%s页---------------(%s/2000)"%(i,i))
    info=parse_html(page)
    save_to_csv(info)

if __name__ == '__main__':
    with open('我主良缘婚姻介绍.csv', 'w', encoding='utf-8-sig')as f:
        f.write('用户id,用户姓名,性别,出生年份,教育水平,省份,城市,身高,收入,婚姻状况,个性签名,\n')

    """开启进程池"""
    start = time.time()
    # 创建数据库
    pool=Pool()
    pool.map(main,range(1,101))
    pool.close()
    pool.join()
    end = time.time()
    print("当前程序的运行时间是:%s秒"%(end-start))















