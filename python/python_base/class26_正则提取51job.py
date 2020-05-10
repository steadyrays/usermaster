import requests,re
from lxml import etree
import pymysql
# 获取网页源代码
def get_html(url):
    header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    try:
        response=requests.get(url,headers=header)
        # 判断网页是否正确返回
        if response.status_code==200:
            return response.content.decode('gbk')
        else:
            print("{0}网页请求状态码错误!{0}".format("-"*10))
    except Exception as e:
        print("{0}请求参数出现错误:{1}{0}".format("-"*10,e))

# 解析网页内容
def parse_html(html):
    pattern=re.compile('<div class="el">.*?title="(.*?)" href="(.*?)".*?title="(.*?)".*?'
                       '"t3">(.*?)<.*?"t4">(.*?)<.*?"t5">(.*?)<.*?</div>',re.S)
    info=re.findall(pattern,html)
    print(info)
    tlist=[]
    for line in info:
        """最低薪酬最高薪酬处理"""
        if line[4][-3:]=="万/月":
            low,high=line[4][:-3].split('-')
            low=float(low)*10000
            high=float(high)*10000
            # print('最低薪酬是%s元,最高薪酬是%s元。'%(low,high))
        elif line[4][-3:]=="千/月":
            low,high=line[4][:-3].split('-')
            low=float(low)*1000
            high=float(high)*1000
            # print('最低薪酬是%s元,最高薪酬是%s元。'%(low,high))
        elif line[4][-3:]=="万/年":
            low,high=line[4][:-3].split('-')
            low=round(float(low)*10000/12,-1)
            high=round(float(high)*10000/12,-1)
        elif line[4]=='':
            low=high=0
        elif line[4][-3:]=='元/天':
            low=high=float(line[4][:-3])*23
        else:
            low=high=0
            print("----------未考虑的情况薪酬:%s---------" % line[4])
        if low==0:
            continue# 跳过添加数据的步骤
        tlist.append([line[0],line[2],line[3].split('-')[0],str(low),str(high),"2019-"+line[5],line[1]])
    print(tlist)
    for line in tlist:
        print(line)
    # return tlist

def save_to_csv(tlist):
    # with open('51job职位信息.csv','a',encoding='utf-8-sig')as f:
    #     for line in tlist:
    #         for word in line:
    #             f.write(word+',')
    #         f.write('\n')
    pass
def main():
    with open('51job职位信息.csv','w',encoding='utf-8-sig')as f:
        f.write("职位名称,公司名称,工作地点,最低薪酬,最高薪酬,发布时间,职位链接,\n")
    for i in range(1,3):
        start_url='https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588,2,{}.html'.format(i)
        html=get_html(start_url)
        print('正在访问第%s页.......' % (i))
        info=parse_html(html)
        # save_to_csv(info)

if __name__ == '__main__':
    main()# 调用主函数



