# # for循环结构
# for 临时变量 in 可迭代对象:
#     语句块...
#     语句块...
#     语句块...
# for i in [1,2,3,5,10,20,100,'a']:# i=1 i=2 i=3
#     print("当前循环i的值为%s"%i)
# print('-'*50)
# for i in (20,100,'a'):# i=1 i=2 i=3
#     print("当前循环i的值为%s"%i)
# print('-'*50)
# for i in 'abc':
#     print("当前循环i的值为%s" % i)
# print('-' * 50)
# for i in '':
#     print("当前循环i的值为%s" % i)

# # 字典的遍历
# d={'name':'韩信','age':18,'job':'刺客'}
# for i in d:
    # print(i,d[i])# 访问到键对象
# print('-' * 50)
# for i in d.keys():
#     print(i)# 访问到键对象
# print('-' * 50)
# for i in d.values():
#     print(i)# 访问到值对象
# print('-' * 50)
# for i,j in d.items():
#     print(i,j)# 同时访问到键对象和值对象

# range()函数
# for i in range(5):# [0,5) 一个参数
#     print("我看完破冰行动第%s集"%(i+1))
# print('-' * 50)
# for i in range(1,101):# [start,end) 两个参数
#     # print(i)
#     print("我看完破冰行动第%s集"%i)
# print('-' * 50)
# for i in range(1,101,3):# (start,end,step) 三个参数
#     print(i)
#     print("我看完破冰行动第%s集"%i)

# 看《倚天屠龙记》55集
# for i in range(55):
#     print("我正在看《倚天屠龙记》第%s集"%(i+1))
    # print(i)
# for i in range(1,56):
#     print("我正在看《倚天屠龙记》第%s集"%i)
    # print(i)

# 1-100的累加和？
# 0+1+2+3+4+5+...+99+100

# s=0
# for i in range(100):
#     s=s+i+1
#     # print(i+1)
# print(s)
#
# s=0
# for i in range(1,101):
#     s=s+i
#     # print(i+1)
# print(s)


# print(sum(range(1,101)))

# 1-100之间奇数的累加和？
# 1+3+5+7+...+97+99
# s=0
# for i in range(1,101,2):
#     # print(i)
#     s=s+i
# print(s)


# 求5的阶乘？
# 1*1*2*3*4*5
# s=1
# for i in range(1,6):
#     s=s*i
#     print(i)
# print(s)

# 遍历列表，打印：我叫name，今年age岁，家住dizhi，电话phone
d = [
    {'name':'小王', 'age':18, 'info':[('phone', '123'), ('dizhi', '广州')]},
    {'name':'小芳', 'age':19, 'info':[('phone', '789'), ('dizhi', '深圳')]},
    {'name':'小杜', 'age':22, 'info':[('phone', '567'), ('dizhi', '北京')]},
    {'name':'小孟', 'age':28, 'info':[('phone', '000'), ('dizhi', '上海')]},
    {'name':'小乔', 'age':26, 'info':[('phone', '111'), ('dizhi', '河南')]},
]
# print('我叫name，今年age岁，家住dizhi，电话phone')
# print(d)
# print(len(d),type(d))
# print(d[0]['name'],d[0]['age'],d[0]['info'][1][1],d[0]['info'][0][1])
# print('我叫%s，今年%s岁，家住%s，电话%s'%
#       (d[0]['name'],d[0]['age'],d[0]['info'][1][1],d[0]['info'][0][1]))
# print('我叫%s，今年%s岁，家住%s，电话%s'%
#       (d[1]['name'],d[1]['age'],d[1]['info'][1][1],d[1]['info'][0][1]))
# print('我叫%s，今年%s岁，家住%s，电话%s'%
#       (d[2]['name'],d[2]['age'],d[2]['info'][1][1],d[2]['info'][0][1]))
# print('我叫%s，今年%s岁，家住%s，电话%s'%
#       (d[3]['name'],d[3]['age'],d[3]['info'][1][1],d[3]['info'][0][1]))
# print('我叫%s，今年%s岁，家住%s，电话%s'%
#       (d[4]['name'],d[4]['age'],d[4]['info'][1][1],d[4]['info'][0][1]))

# for i in range(5):
#     print('我叫%s，今年%s岁，家住%s，电话%s' %
#           (d[i]['name'], d[i]['age'], d[i]['info'][1][1], d[i]['info'][0][1]))
# print("-"*50)
# for i in d:
#     # print(i['name'],i['age'],i['info'][1][1],i['info'][0][1])
#     print('我叫%s，今年%s岁，家住%s，电话%s'%
#           (i['name'],i['age'],i['info'][1][1],i['info'][0][1]))

# 1！+2！+3！+4！+5！
# 1+2+3+4+5

# h=1
# for j in range(1,6):
#     h=h*j
# print(h)

# s=0
# for i in range(1,6):
#     h=1
#     for j in range(1,i+1):
#         h=h*j
#     s=s+h
# print(s)

# i=1# 创建循环次数的变量
# s=1
# c=0# 累加的变量
# while i<=5:# 0+1！+2！+3！+4！+5！
#     s=s*i# 求阶乘
#     i+=1
#     c+=s
# print(c)
#
# s=1
# c=0
# for i in range(1,6):
#     s=s*i
#     # print(i)
#     c=c+s
# print(c)

# for i in range(5):
#     for j in range(5):
#         print('当前循环i的值为%s,j的值为%s'%(i,j))

# 找到2-100之间所有的素数,并且保存到列表中 2 3 4 5 6 10 12 11 13
# 素数:只能整除1和自己本身

result=[]
for i in range(2,101):
    charge=True
    for j in range(2,i):
        if i%j==0:
            # 能整除不是素数
            result.append(i)
            # print("%s不是一个素数"%i)
            # charge=False
            break
print(result)
num=list(range(2,101))
for i in result:
    num.remove(i)
print(num)















