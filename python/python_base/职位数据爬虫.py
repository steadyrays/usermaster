import requests
from lxml import etree
import pymysql
import re
import json
import time
f1=open('code.txt','r',encoding='utf-8').read()
coms=re.compile('{"name":".*?","en_name":".*?","code":"(.*?)","sublist":.*?}',re.S)
ress=re.findall(coms,f1)
for n in ress:
    # time.sleep(2)
    dl = {'HTTP': '125.123.127.121:9000'}
    url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId={}&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3&_v=0.65144709&x-zp-page-request-id=9cd946e959964b84aba57a7649937902-1567145279094-874674&x-zp-client-id=365c95b9-f35e-423a-93d5-358b9a24b8e6'.format(n)
    response=requests.get(url,proxies=dl)
    data=response.content.decode('utf-8')
    try:
        # #正则表达式解析
        # com=re.compile('{"number":.*?"rate":".*?"}')
        # '{"number":.*?"rate":".*?"}'
        # re1=re.findall(com,data)
        # print(re1[1])
        #json解析
        datas=json.loads(data) #将json转换为字典格式
        for i in datas['data']['results']:
            jobname=i['jobName']
            gsname=i['company']['name']
            city=i['city']['display']
            money=i['salary']
            jy=i['workingExp']['name']
            xl=i['eduLevel']['name']
            fl=str(i['welfare'])
            gsgm=i['company']['size']['name']
            zwurl=i['positionURL']
            #再次请求第二层信息
            res=requests.get(zwurl)
            datas1=res.content.decode('utf-8')
            html=etree.HTML(datas1)
            gsxz=html.xpath('//div/button[@class="company__industry"]/text()')
            tabel=[]
            if len(gsxz)>0:
                tabel.append([jobname,gsname,city,money,jy,xl,fl,gsgm,gsxz[0]])
            else:
                tabel.append([jobname,gsname,city,money,jy,xl,fl,gsgm,''])
            #解析任职信息
            zwxx=html.xpath('//div[@class="describtion__detail-content"]//text()')
            #匹配技能信息
            com=re.compile('excel|spss|python|mysql|sql|ppt|office|r|sas|pivot|hive|hadoop|tableau|java|c/+/+|分析|挖掘|php|net|bi|linux|etl|eviews|erp|oracle|crm|html|spark',re.S)
            re2=re.findall(com,str(zwxx).lower())
            tabel[0].append(str(set(re2)))
            #匹配专业
            com1=re.compile('统计|数学|计算机|金融|经济|软件工程|信息|英语|软件|财务|商务|会计')
            re3=re.findall(com1,str(zwxx))
            tabel[0].append(str(set(re3)))
            #保存数据
            conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='class_06',charset='utf8')
            cursor=conn.cursor()
            sql='insert into `职位信息数据表` values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.executemany(sql,tabel)
            conn.commit()
            cursor.close()
            conn.close()
            with open('职位信息.txt','a',encoding='utf-8') as f:
                f.writelines(zwxx)
                f.write('\n'+'='*100+'\n')
            print('保存《%s》完成' % gsname)
    except:
        continue




















