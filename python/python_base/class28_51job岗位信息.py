import requests,re
from lxml import etree
from multiprocessing import Pool# 进程池
import time,random
# 1、通过url获得网页源代码
# 2、解析网页源代码得到所有页面的链接
# 3、循环访问url获得网页源代码
# 4、解析详细页面信息,提取字符串
# 5、写入本地文件txt
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

def get_urls(html):# 获取网页中所有详细信息的链接
    html=etree.HTML(html)
    url_list=html.xpath('/html/body/div[2]/div[4]/div[@class="el"]/p/span/a/@href')
    return url_list

def get_job_info(html):
    html=etree.HTML(html)
    """获取职位信息"""
    zwmc=html.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/@title')[0]
    gsmc=html.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]/@title')[0]
    strong=html.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()')
    if strong:
        xc=strong[0]
    else:# None
        xc='未知'
    # print(zwmc,gsmc,xc)

    """获取职位要求"""
    p=html.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]')[0]
    info1=p.xpath('string(.)').strip()# 工作经验 学历要求
    # print(info1)

    """获取岗位信息"""
    div=html.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div')[0]
    # print(div.xpath('string(.)'))
    info2=re.sub("\s{3,}","  ",div.xpath('string(.)')).strip()
    return zwmc,gsmc,xc,info1,info2# 返回工作岗位信息,元组类型


def save_to_txt(tup):# 保存文档
    with open('51job岗位信息.txt','a',encoding='utf-8')as f:
        f.write('%s %s %s\n'%(tup[0],tup[1],tup[2]))# 写入招聘信息
        f.write(tup[3]+'\n')# 写入职位信息
        f.write(tup[-1])# 写入岗位要求
        f.write('\n\n\n')

def main(i):
    start_url='https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588,2,{}.html?'.format(i)
    print("当前正在访问%s页........"%i)
    html=get_html(start_url)
    url_list=get_urls(html)
    for url in url_list:
        info_html=get_html(url)
        try:
            job_info=get_job_info(info_html)
            save_to_txt(job_info)
        except:
            print("{0}一条网页信息进行跳转:{1}".format('-> '*10,url))
            continue
if __name__ == '__main__':
    with open('51job岗位信息.txt', 'w', encoding='utf-8')as f:
        f.write('')
    """开启进程池"""
    start=time.time()
    pool=Pool()
    pool.map(main,range(1,101))
    pool.close()
    pool.join()
    end=time.time()
    print("当前程序的运行时间是:%s秒"%(end-start))
# 爬取30页
# 多进程提高效率
# 请分析我们的职业技能






