import random

# print(random.random())# 随机生成0-1之间的随机数
# for i in range(10):
    # print(random.random())# 随机生成0-1之间的随机数

    # print(random.randint(1,3))# 随机生成1-3之间的随机整数(左闭右闭)

    # print(random.uniform(1,3))# 随机生成1-3之间的随机浮点数
# random.shuffle打乱一个序列的顺序
# l=['小a','小b','小c','小d','小e']
# random.shuffle(l)# 没有生成对象而是直接改变了序列
# print(l)

# random.choice(l)从一个序列中随机抽取一个元素
# print(random.choice(l))
# print("有请学号为%s号的同学上台回答问题。"%random.choice(range(1,101)))

# print(random.sample(l,4))# 从一个序列中随机抽取n个元素,返回列表
# 有放回抽样和无放回抽样
# print("有请学号为%s号的同学上台回答问题。"%random.choice(range(1,101)))
# print("有请学号为11、22、43、57号的同学上台回答问题。")
# 定义一个函数实现抽取多个同学回答问题的操作
# def choice_stu(n):
#     slist=sorted(random.sample(range(1,101),n))
#     print(slist)# 第1步
#     stringlist=list(map(lambda x:str(x)+'号',slist))
#     print(stringlist)# 第2步
#     info='、'.join(stringlist)
#     print(info)
#     print("有请学号为%s的同学上台演讲。"%info)
# choice_stu(10)

# 对列表元素做处理
# a=[1,2,3,4,5]
# new=[]
# for i in a:# 普通循环循环
#     new.append(str(i))
# print(new)

# print(list(map(lambda x:str(x),a)))# map映射操作

# # 猜数字的游戏,让用户从1-100之间猜数字,如果大于设定的数字则提示猜大了,如果小于设定的数字则提示猜小了
# random input if while break
# print('----------猜数字游戏开始----------')
# start = random.randint(1, 100)  # 50
# # print(start)
# while True:
#     try:
#         guess=int(input("请输入一个1-100之间的整数:"))
#         # 为什么输入某些信息会报错
#         # 不在1-100的范围内怎么处理
#         if guess not in range(1,101):
#             print("输入数字不在1-100之间!")
#         elif guess>start:
#             print("猜大了!")
#         elif guess<start:
#             print("猜小了")
#         else:
#             print("恭喜你猜对了!")
#             break
#     except:
#         print("输入信息错误!")
# print('----------猜数字游戏结束----------')



import time
# 获取当前时间戳,从1970年1月1日开始经历过的秒数
# print("获取当前时间戳:%s"%time.time())
# print(time.time()/60/60/24/365)

# 时间戳转时间元组
# print("获取时间元组:",time.localtime())
# print(time.localtime(time.time()-60*60*24))
# year month day hour minute second week
p_tuple=time.localtime()
# print(p_tuple.tm_year,p_tuple.tm_wday,p_tuple.tm_mon,p_tuple.tm_yday)# 调用属性

# 时间元组转字符串format
# print(time.strftime("%Y-%m-%d",p_tuple))
# print(time.strftime("%Y/%m/%d %H:%M:%S",p_tuple))

# 字符串转时间元祖parse
# time.strptime(string,format)
# print(time.strptime("2019-6-18 12:05:34","%Y-%m-%d %H:%M:%S"))

# 时间元组转时间戳
# print(time.mktime(p_tuple))

# 时间戳- localtime -> 时间元组- strftime -> 字符串
# 字符串- strptime -> 时间元组- mktime -> 时间戳
from time import *
start_time='2019/02/05 23:55:00'
# 看了两个小时34分的春节节目就不看了，那计算一下这个时间是什么样的，
# 要求以'xxxx-xx-xx xx:xx:xx'的形式返回
# str-->秒数-->计算秒数+2*小时+34*分钟-->str
# 字符串-->时间元组
tup1=strptime(start_time,"%Y/%m/%d %H:%M:%S")
# 时间元组-->时间戳
sec1=mktime(tup1)
# 时间计算
sec2=sec1+2*60*60+34*60
# 时间戳-->时间元组
tup2=localtime(sec2)
# 时间元组-->字符串
end=strftime("%Y-%m-%d %H:%M:%S",tup2)
# print("最终时间为:%s"%end)
end=strftime("%d/%m/%Y %H:%M:%S",tup2)
# print("最终时间为:%s"%end)

import time
# 作业
# 1、时间转化
# 给你一个Date 2019-06-18时间,怎么变成2019年6月18日？
t1="2019-06-18"
t1_tuple=time.strptime(t1,"%Y-%m-%d")
t1_str=time.strftime("%Y{}%m{}%d{}",t1_tuple)
# print(t1_str.format("年","月",'日'))

# start_time='2019-06-18'
# i=time.strptime(start_time,'%Y-%m-%d')
# print('%s年%s月%s日'%(i.tm_year,i.tm_mon,i.tm_mday))

# 2、给你一个时间，打印输出他是星期几
# t="2019-06-17" ---> 输入的日期是星期一
# t="2019-06-18" ---> 输入的日期是星期二
# 星期六 星期日
t="2019-06-17"
d ={0: "星期一", 1: "星期二", 2: "星期三",3: "星期四",4: "星期五", 5: "星期六", 6: "星期日"}
t_tuple=time.strptime(t,"%Y-%m-%d")
wday=t_tuple.tm_wday# 0 1 2 3 4 5 6
ds='一二三四五六日'
dl=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
# print("输入日期为:%s,这一天是%s"%(t,d[wday]))
# print("输入日期为:%s,这一天是星期%s"%(t,ds[wday]))
# print("输入日期为:%s,这一天是%s"%(t,dl[wday]))

# 3、Jun/18/19 --> 2019-6-18
# 自主查询1-12月份的缩写
# 将英文时间转换成目标格式

# 4、将目标txt文件重写为csv类型
# f=open("C:\Users\ibf\Desktop\工程品管 IDL 门禁记录.txt")

# 5、怎么优化猜数字游戏?


#时间戳
time.time()
#时间戳转时间元组
time.localtime()
#时间元组转字符串
time.strftime()
#字符串转时间元组
time.strptime()
#时间元组转时间戳
time.mktime()



































