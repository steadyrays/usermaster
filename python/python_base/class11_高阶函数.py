# 函数的参数包含另一个函数时,为高阶函数
# filter函数的定义
# filter(function,iterable)
l=list(range(1,101))
def f(data):
    if data%2==1:
        return True# 想要筛选下来的信息返回True
    else:
        return False# 想要筛选掉的信息返回False
# print(list(filter(f,l)))

# 练习
nlist=[1,1,2,1,2,2,3,4,5,2,1]
# 利用筛选函数去除所有的2
def f1(data):
    if data==2:
        return False
    else:
        return True
# for i in filter(f1,nlist):
#     print(i)
# print(list(filter(f1,nlist)))

slist=['abc','ABC','nba','CBA']
# 利用筛选函数去除都是小写的字母的信息.islower()
def f2(data):
    if data.islower():
        return False
    else:
        return True
# print(list(filter(f2,slist)))

# 求将这个列表中所有2018年7-8月份1-15号的日期数据提取出来
# 2018-7-1 ~2018-7-15
# 2018-8-1 ~2018-8-15
# t=['2016-5-12','2016-7-15','2016-11-11','2017-6-8','2017-12-12'\
#    ,'2018-1-1','2018-2-2','2018-7-2','2018-8-2','2018-9-2','2018-11-18']
# def f3(data):
#     year=int(data.split('-')[0])
#     month=int(data.split('-')[1])
#     day=int(data.split('-')[2])
#     # year,month,day=data.split('-')
#     if year==2018 and (month==7 or month==8) and day in range(1,16):
#         return True
#     else:
#         return False
# print(list(filter(f3,t)))

# map映射函数
# map(function,iterable1,iterable2,....)
l=[1,2,3,4,5]
# print(list(map(lambda x:x**2,l)))
# print(list(map(lambda x:x*2,l)))
# print(list(map(lambda x:x+2,l)))
# print(list(map(lambda x:x-2,l)))
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
# print(list(map(lambda x,y:x+y,l1,l2)))
l3=[1,2,3,4,5]
l4=['星期1','星期2','星期3','星期4','星期5']
# print(list(map(lambda x:'星期'+str(x),l3)))


# reduce函数
import functools
# functools.reduce(function,sequence)
r=functools.reduce(lambda x,y:x+y,[1,2,3,4,5])
# print(r)
r=functools.reduce(lambda x,y:x*y,[1,2,3,4,5])
# print(r)

# sorted()函数
l=[5,4,1,2,10,-10,8]
# print(sorted(l))# 默认升序
# print(sorted(l,reverse=True))# 降序

string='aaaaabbbbccccccdddddeeeeeefffffff'
# string=['a','b','a','b','c']
# a-出现次数
# b-出现次数
# c-出现次数
# d={}
# for i in string:# 统计序列中元素出现次数
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]=d[i]+1
# print(d)
# print(sorted(d.items(),key=lambda x:x[1]))
# print(sorted(d.items(),key=lambda x:x[0]))

# import collections
# c=collections.Counter(string)# 对序列元素进行统计
# print(c)

# map>filter>sorted>reduce

# # 给你一个正整数,打印如下图形
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 ....
n=27
a=1
b=2
# 初始值a=1 每次累加一个变量b(2,3,4,5,6,....)
# for i in range(1,n+1):
#     print(i,end=' ')
#     # 1 3 6 10 15 21
#     if i==a:
#         print()
#         a+=b# 2 3 4
#         b+=1

# 题目4：将一个正整数分解质因数。例如：输入90, 打印出90 = 2 * 3 * 3 * 5。程序分析：对n进行分解质因数，

# 6=2*3
# 8=2*2*2
# 9=3*3
# 12=2*2*3
# 20=2*2*5
# 100=2*2*5*5
# 144=2*2*2*2*3*3
# 144=2*2*2*2*3*3
# a=[2,2,2,2,]
# num=int(input("请输入一个正整数:"))
# num1=num# 创建一个副本
# result=[]
# while True:# 不断尝试寻找因子
#     for i in range(2,int(num)+1):#
#         if num%i==0:
#             result.append(i)
#             num=num/i# 1
#             break
#             # 重新进入for循环
#     if num==1:# 当无法因式分解时num等于1
#         break
# if len(result)!=1:
#     r="*".join(map(lambda x:str(x),result))
#     print("%s=%s"%(num1,r))
# else:
#     print("%s=1*%s"%(num1,result[0]))





