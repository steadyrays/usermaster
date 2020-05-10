"""第六题"""
# 已有文件51job岗位信息.txt,请从文件中提取出每个岗位的如下信息:
# 职位名称、公司名称、最低薪酬、最高薪酬、工作城市、经验要求、学历要求、所需常用软件技能
# excel、tableau、hive、mysql、sql server、python
# 数据保存在数据库中
# Tips:若不存在此信息,字符串类型默认为空,薪酬未标明或者异常可以默认设置为0

# 职位名称、公司名称、最低薪酬、最高薪酬、
# 工作城市、经验要求、学历要求、
# 所需常用软件技能
import re
sql_data=[]
"""第1步:读取数据"""
with open("51job岗位信息.txt",'r',encoding='utf-8')as f:
    job_str=f.read().strip()
"""第2步:分割出每一条数据"""
# job_info=job_str.split("\n\n\n")
job_info=re.split("\n{3,}",job_str)
count=[]
for info in job_info:
    try:
        line1,line2,line3=info.split('\n')
        # print(line1,line2,line3,sep='\n')
        # if len(line1.split(' '))!=3:
        #     print(len(line1.split(' ')))
        #     print(line1.split(' '))
        #     print("- - "*50)
        """第一行信息"""
        line1_split=line1.split()
        zwmc=' '.join(line1_split[:-2])
        gsmc=line1_split[-2]
        """最低薪酬最高薪酬处理"""
        if line1_split[-1][-3:]=="万/月":
            low,high=line1_split[-1][:-3].split('-')
            low=float(low)*10000
            high=float(high)*10000
            # print('最低薪酬是%s元,最高薪酬是%s元。'%(low,high))
        elif line1_split[-1][-3:]=="千/月":
            low,high=line1_split[-1][:-3].split('-')
            low=float(low)*1000
            high=float(high)*1000
            # print('最低薪酬是%s元,最高薪酬是%s元。'%(low,high))
        elif line1_split[-1][-3:]=="万/年":
            low,high=line1_split[-1][:-3].split('-')
            low=round(float(low)*10000/12,-2)
            high=round(float(high)*10000/12,-2)
        elif line1_split[-1]=='':
            low=high=0
        elif line1_split[-1][-3:]=='元/天':
            low=high=float(line1_split[-1][:-3])*23
        else:
            low=high=0
            # print("----------未考虑的情况薪酬:%s---------"%line1_split[-1])


        """第二行信息"""
        # 城市 工作经验  学历
        length=len(line2.split("|"))
        line2_split=line2.split("|")
        # if line2_split==7:# 4:缺少学历要求 5:正常情况  6、7:额外的要求
        #     print(line2)# 4 5 6 7
        city=line2_split[0].split("-")[0]
        jy=line2_split[1]
        if length==5:
            xl=line2_split[2]
        elif length==4:
            xl='未要求'
        elif length==6 or length==7:
            xl=line2_split[2]
        else:
            xl='未知'
            # print(xl)

        """第三行信息"""
        # print(line3)
        pattern1=re.compile("c\+\+|SQL\sServer",re.I)
        pattern2=re.compile("[a-zA-Z]+",re.I)
        skills_01=re.findall(pattern1,line3)
        skills_02=re.findall(pattern2,line3)
        skills=skills_02+skills_01

        # 字符元素全部小写
        skills=map(lambda x:x.lower(),skills)

        # 技能筛选
        # 读取技能词典
        with open('技能词典.txt','r',encoding='utf-8')as f:
            skill_list=f.read().split(',')
        def ft(data):
            if data in skill_list:
                return True
            else:
                return False
        skills=set(filter(ft,skills))
        # print(skills)# sql、excel、python
        # count.append(line2_split)
        sql_data.append([zwmc,gsmc,low,high,city.strip("\xa0"),jy.strip("\xa0"),xl.strip("\xa0"),'、'.join(skills)])
    except:
        # 爬虫非正常获取的数据
        # print("非正常数据:%s"%info)
        continue

import pymysql
conn=pymysql.connect(host='localhost',user='root',password='123456',db='class_06',charset='utf8')
cursor=conn.cursor()
create_sql="""create table if not exists job_info(`职位名称` varchar(255) not null,`公司名称` varchar(255) not null,
`最低薪酬` float not null,`最高薪酬` float not null,`城市` varchar(255) not null,`经验` varchar(255) not null,
`学历` varchar(255) not null,`技能`varchar(255) not null)
"""
cursor.execute(create_sql)
conn.commit()
insert_sql="""insert into job_info values(%s,%s,%s,%s,%s,%s,%s,%s)"""
cursor.executemany(insert_sql,sql_data)
conn.commit()
cursor.close()
conn.close()
# for data in sql_data:
#     print(data)












