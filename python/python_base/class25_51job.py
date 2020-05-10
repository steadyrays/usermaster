
import requests
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
    html=etree.HTML(html)
    # 获取职位名称
    zwmc=html.xpath('/html/body/div[2]/div[4]/div[@class="el"]/p/span/a/text()')
    # print(zwmc)
    # 获取公司名称
    gsmc=html.xpath('/html/body/div[2]/div[4]/div[@class="el"]/span[1]/a/text()')
    # print(gsmc)
    # 获取工作地点
    gzdd=html.xpath('/html/body/div[2]/div[4]/div[@class="el"]/span[2]/text()')
    # print(gzdd)
    # 获取薪酬
    xc=html.xpath('/html/body/div[2]/div[4]/div[@class="el"]/span[3]')
    XC=[]
    for i in xc:
        XC.append(i.xpath('string(.)'))
    # 获取发布时间
    fbsj=html.xpath('/html/body/div[2]/div[4]/div[@class="el"]/span[4]/text()')
    # print(fbsj)
    tlist=[]
    # print(len(zwmc),len(gsmc),len(gzdd),len(fbsj),len(XC))
    for i in range(len(zwmc)):
        if XC[i][-3:]=="万/月":
            low,high=XC[i][:-3].split('-')
            low=float(low)*10000
            high=float(high)*10000
            # print('最低薪酬是%s元,最高薪酬是%s元。'%(low,high))
        elif XC[i][-3:]=="千/月":
            low,high=XC[i][:-3].split('-')
            low=float(low)*1000
            high=float(high)*1000
            # print('最低薪酬是%s元,最高薪酬是%s元。'%(low,high))
        elif XC[i][-3:]=="万/年":
            low,high=XC[i][:-3].split('-')
            low=float(low)*10000/12
            high=float(high)*10000/12
        elif XC[i]=='':
            low=high=0
        elif XC[i][-3:]=='元/天':
            low=high=float(XC[i][:-3])*23
        else:
            low=high=0
            print("----------未考虑的情况薪酬:%s---------"%XC[i])
        tlist.append([zwmc[i].strip(),gsmc[i],gzdd[i].split('-')[0],low,high,'2019-'+fbsj[i]])
    # for line in tlist:
    #     print(line)
    return tlist

def create_table():
    conn=pymysql.connect(host='localhost',user='root',password='123456',db='class_06',charset='utf8')
    cursor=conn.cursor()
    create_sql="""create table if not exists 51_job(zwmc varchar(255) not null,gsmc varchar(255)
    not null,gzdd varchar(255) not null,low_salary float not null,high_salary float not null,
    fbsj date not null)"""
    cursor.execute(create_sql)0
    print("{0}正在创建数据库{0}".format('-'*15))
    conn.commit()# 提交事务
    cursor.close()
    conn.close()

# 保存到本地
def save_to_mysql(tlist):
    conn=pymysql.connect(host='localhost',user='root',password='123456',db='class_06',charset='utf8')
    cursor=conn.cursor()
    insert_sql="insert into 51_job values(%s,%s,%s,%s,%s,%s)"
    for line in tlist:
        cursor.execute(insert_sql,line)
    conn.commit()# 提交事务
    cursor.close()
    conn.close()

def main():
    create_table()
    for i in range(1,11):
        start_url='https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(i)
        html=get_html(start_url)
        print('正在访问第%s页.......' % (i))
        info=parse_html(html)
        save_to_mysql(info)

if __name__ == '__main__':
    main()# 调用主函数














