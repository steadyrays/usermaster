# 练习1
# for i in range(5):
#     print(i,i,i,i,i)
#
# for i in range(5):
#     s=str(i)+' '
#     print(s*5)

# # 练习2
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# for i in range(1,6):
#     # print(i)# 5--》5!  5 --> 1 2 3 4 5
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()

# for i in range(5):
#     print(i)
# 5 --> 1 2 3 4 5
# z=''
# for i in range(1,6):# 1!+2!+3!+4!+5!
#     z=z+' '+str(i)
#     print(z)

# for i in range(1,6):
#     print(i)
# 5 --> 1 2 3 4 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# # 给你一个正整数,打印如下图形
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 ....

# # 求第100个值
# 1 1 2 3 5 8 13 21 34 ...


# 练习3
# 已知大公鸡5元，母鸡3元，小鸡1元3个。（百元买百鸡）
# 5x+3y+z/3=100
# x+y+z=100
# time=0
# for x in range(0,21):#  20*33*100
#     for y in range(0,34):
#         for z in range(0,101):
#             time+=1
#             if x+y+z==100 and 5*x+3*y+z/3==100:
#                 print("公鸡买%s只,母鸡买%s只,小鸡买%s只"%(x,y,z))
# print(time)
# time=0
# for x in range(0,21):#  21*34
#     for y in range(0,34):
#         time+=1
#         if 5*x+3*y+(100-x-y)/3==100:
#             print("公鸡买%s只,母鸡买%s只,小鸡买%s只"%(x,y,100-x-y))
# print(time)
#
# time=0
# for x in range(0,21):#  21*34
#     for y in range(0,(100-x*5)//3):
#         time+=1
#         if 5*x+3*y+(100-x-y)/3==100:
#             print("公鸡买%s只,母鸡买%s只,小鸡买%s只"%(x,y,100-x-y))
# print(time)

# # 打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s'%(j,i,i*j),end=' ')
#     print()

# # 用while循环写九九乘法表
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print("%s*%s=%s"%(j,i,i*j),end=' ')
#         j+=1
#     print()# 换行
#     i+=1

# 写一个用户登录的循环语句，要求如下
# 用户信息保存在user字典中，如user={'老王':‘123456’,'小明':‘987654’}
# 其中键对象为用户名，值对象为密码，要求利用循环语句完成用户登录
# 每次登录先进行用户姓名确认，如果正确后再进行密码确认，如果用户和密码验证失败，则继续进行输入
# 知道完成登录，或者输入信息次数超过5次

# 1、用户信息保存在字典user中
# 2、让用户输入用户名,如果用户名在字典中则让用户输入密码,如果密码正确,显示登录成功
# 3、如果密码错误显示密码错误请重新登录
# 4、如果用户名不存在字典中则提示用户用户名不存在，然后让用户重新登录
# 5、假如登录次数超过5次则锁定账号，那么用户再也无法登录
print("--------用户登录验证开始---------")
user={'老王':{'password':'123456','money':5000},'小明':{'password':'456789','money':1500}}
count=0
while True:
    user_name=input("请输入你的用户名:")
    if user_name in user:# 用户名存在
        print("用户名存在!")
        while True:
            password=input("请输入你的密码:")
            if password==user[user_name]['password']:
                # Tab向后 Shift+Tab向前
                print("密码正确,登录成功!")
                while True:
                    money=int(input("请输入提取金额:"))
                    if money<=user[user_name]['money']:# money 'money'
                        print("提取成功!")
                        break
                    else:
                        print("余额不足!")
                        while True:
                            word=input("你是否需要继续取款(是/否):")
                            if word in ['是','否']:
                                break
                            else:
                                print("输入信息错误!")
                        if word=="否":
                            break
                # input()# 输入金额
                # if # 判断金额和余额的大小
                # 余额不足时需要重新输入金额while

                # 请输入提款金额,如果金额小于余额,可以正常提款
                # 如果大于余额,无法正常提取请重新输入提取金额
                # 正常提取金额后程序结束
                break
            else:
                count+=1# 1 2 3 4 5
                if count>=5:
                    print("输入信息错误超过5次,账号已锁定!")
                    break
                print("密码错误,请重新输入密码!")
        # 再次跳出循环
        break
    else:# 用户名不存在
        count+=1# 1 2 3 4 5
        if count>=5:
            print("输入信息错误超过5次,账号已锁定!")
            break# 不能进入下一次循环
        print("用户名不存在,请重新输入!")
print("--------用户登录验证结束---------")


# print("--------用户登录验证开始---------")
# user={'老王':'123456','小明':'987654'}
# count=0
# while True:
#     user_name=input("请输入你的用户名:")
#     password=input("请输入你的密码:")
#     if user_name in user:# 用户名存在
#         print("用户名存在!")
#         if password==user[user_name]:
#             print("密码正确,登录成功!")
#             break
#         else:
#             count+=1
#             if count >=3:
#                 print("输入信息错误超过3次,账号已锁定!")
#                 break
#             print("密码错误,重新登录!")
#     else:# 用户名不存在
#         count+=1# 1 2 3 4 5
#         if count>=3:
#             print("输入信息错误超过3次,账号已锁定!")
#             break# 不能进入下一次循环
#         print("用户名不存在,请重新输入!")
# print("--------用户登录验证结束---------")








