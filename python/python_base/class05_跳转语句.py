# 跳转语句:break语句和continue语句
# print("---------break跳转语句开始--------")
# i=1
# while i<=10:
#     if i%5==0:
#         print("满足条件跳出整个循环")
#         break
#     print('当前是第%s次循环'%i)
#     i+=1
# print("---------break跳转语句结束--------")

# print("---------continue跳转语句开始--------")
# i=0
# while i<=9:
#     i+=1
#     if i==5:
#         # print("满足条件跳出整个循环")
#         continue
#     print('当前是第%s次循环' % i)
# print("---------continue跳转语句结束--------")

# print("---------break跳转语句开始--------")
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)
# print("---------break跳转语句结束--------")
#
# print("---------continue跳转语句开始--------")
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)
# print("---------continue跳转语句结束--------")

# break
# 有一根长度为3000米的绳子,每天减去一半,请问多少天后绳子的长度小于5米?
# 3000 1500 750 375 ... <5
# while for
# long=3000
# day=0

# print("---------while语句开始--------")
# while long>=5:
#     long=long*0.5
#     day+=1
# print("当第%s天的时候绳子的长度为%s米"%(day,long))
# print("---------while语句结束--------")

# long=3000
# day=0
# print("---------while语句开始--------")
# while True:# while 1:
#     long=long*0.5
#     day+=1
#     if long<5:
#         break
# print(day)
# print("当第%s天的时候绳子的长度为%s米"%(day,long))
# print("---------while语句结束--------")

# 求1-100之间所有的奇数
# s=0
# for i in range(1,101):
#     if i%2==0:
#         continue
#     # print(i)
#     s=s+i
# print(s)

# num=[1,2,3,10,9,0,19,20]
# for i in num:
#     if i==0:
#         continue
#     print(10/i)


# 找到2-100之间所有的素数,并且保存到列表中 2 3 4 5 6 10 12 11 13
# 素数:只能整除1和自己本身
# result=[]
# for i in range(2,101):
#     charge=True
#     for j in range(2,i):
#         if i%j==0:
#             # 能整除不是素数
#             # result.append(i)
#             print("%s不是一个素数"%i)
#             charge=False
#             break
#     if charge:
#         result.append(i)
# print(result)
# a=set(range(2,101))
# b=set(result)
# print(a-b)
# 5 7 11 13
# 5:2 3 4
# 7:2 3 4 5 6
# 9:2 3
# 11:2 3 4 5 6 7 8 9 10
# 23:2 3 4 5 6 7 8 9 10 ... 20 21 22
# 4 6 8 9


