# 异常会中断我们的程序运行
# 想想遇到过哪些异常?
# 类型错误
# print('123'+123)# TypeError: must be str, not int

# 语法错误
# for i in range(10)# SyntaxError: invalid syntax
#     print(i)

# 缩进错误
# if True:# IndentationError
#     print(1)
#      print(2)

# 名称错误
# print(true)# NameError: name 'true' is not defined

# 属性错误
# print(list.append)# AttributeError: type object 'dict' has no attribute 'append'
# print(dict.append)

# 索引错误
# a=[1,2,3,4]# IndexError: list index out of range
# print(a[10])

# ZeroDivisionError
# print(10/0)# ZeroDivisionError: division by zero

# # TypeError
# a='abc'
# a[0]='A'# TypeError: 'str' object does not support item assignment

# # KeyError:'c'
# d={'a':1,'b':2}
# d['c']

# try:
#     代码块1
# except:
#     代码块2

# num=[10,20,1,20,0,8,0,5]
# for i in num:
#     try:
#         # print(num[i])
#         print(10/i)
#     except:
#         print("出现异常情况!")
#     # except Exception as e:
#     #     print("出现异常情况是%s"%e)
#     else:
#         print("try语句后的代码正常运行时执行")
    # finally:
    #     print("无论什么情况,都会运行finally后的语句")



# 闰年的判断
# while True:
#     try:
#         year=int(input("请输入一个年份:"))
#         if (year%4==0 and year%100!=0) or year%400==0:
#             print("%s是一个闰年"%year)
#             break
#         else:
#             print("%s不是一个闰年"%year)
#             break
#     except:
#         print("输入信息类型错误!")


# # 练习:用户登录练习
# 输入用户名和密码,进行登录判断(先判断用户名,再判断密码)
# user password
# while True:
#     user_info={'老王':12345678,'小明':88888888,'小张':66666666}
#     user=input("请输入你的用户名:")
#     password=input("请输入你的密码:")
#     if user in user_info:
#         print("用户名存在!")
#         try:
#             if int(password)==user_info[user]:# 判断密码是否正确
#                 print("恭喜你,登录成功!")
#                 break
#             else:
#                 print("密码输入错误!")
#         except:
#             print("输入密码类型不正确!")
#     else:
#         print("用户名不存在!")








