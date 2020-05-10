# if 条件表达式:
#     语句块...
#     语句块...
#     语句块...
# print("---------if语句判断开始--------")
# age=19
# if age>=18:
#     print("你已经成年了!")
#     print("你可以去网吧!")
#     print("你可以谈恋爱!")
#     # Tab生成一个缩进,shift+Tab取消缩进
# print("---------if语句判断结束--------")


# print("---------if语句判断开始--------")
# age=17
# if age>=18:
#     print("判断通过!")
# if False:
#     print("判断通过!")
# if 0:
#     print("判断通过!")
# if None:
#     print("判断通过!")
# if 'abc':
#     print("判断通过!")
# if [1,2,3]:
#     print("判断通过!")
# if {'a':1}:
#     print("判断通过!")
# # 条件表达式的值为False的情况如下：
# # False、0、None、空字符串、空列表、空元组、空集合、空字典、
# # 空的range和迭代对象
#
# # 除了以上情况外，均为True！！！
# print("---------if语句判断结束--------")

# if-else语句
# 结构:
# if 条件表达式:
#     语句块1
# else:
#     语句块2

# age=16
# if age>=18:
#     print("你已经成年了!")
# else:
#     print("你还是未成年,请好好读书!")
# print("---------if语句判断开始--------")
# age=int(input("请输入你的年龄:"))
# if age>=18:
#     print("你可以去游览王者峡谷了!")
# else:
#     print("你还未成年,有防沉迷限制,每天只能玩2小时!")
# print("---------if语句判断结束--------")


# if-elif-else语句
# print("---------if语句判断开始--------")
# score=97
# if score>=90:
#     print("你的评分等级是A")
# elif score>=80:
#     print("你的评分等级是B")
# elif score>=70:
#     print("你的评分等级是C")
# elif score>=60:
#     print("你的评分等级是D")
# else:
#     print("你的评分等级是E")
# print("---------if语句判断结束--------")

# if的嵌套语句
# if 条件1:
#     if 条件2:
#         语句1
#     else:
#         语句2
# else:
#     语句3
# anjian=False
# mp=True
# if anjian:
#     print("你已经通过了安检!")
#     if mp:
#         print("你有地铁票,可以去搭乘地铁!")
#     else:
#         print("你没有票,请到服务台办理!")
# else:
#     print("你没有通过安检,不能搭乘地铁!")

# # 练习:用户登录练习
# # 输入用户名和密码,进行登录判断(先判断用户名,再判断密码)
# # user password
# user_info={'老王':12345678,'小明':88888888,'小张':66666666}
# user=input("请输入你的用户名:")
# password=input("请输入你的密码:")
# if user in user_info:
#     print("用户名存在!")
#     if int(password)==user_info[user]:# 判断密码是否正确
#         print("恭喜你,登录成功!")
#     else:
#         print("密码输入错误!")
# else:
#     print("用户名不存在!")

# # 练习2:年龄段的判断
# age=int(input("请输入你的年龄:"))
# if age<7:# 1-6
#     print("你应该去幼稚园!")
# elif age<13:# 7-12
#     print("你应该上小学了!")
# elif age<19:# 13-18
#     print("你应该上中学了!")
# elif age<23:# 19-22
#     print("你应该上大学了!")
# else:
#     print("你可能读研或者进入社会了!")


# 练习3:闰年的判断
# 能被4整除并且不能被100整除 或者 能被400整除
# 2008是 2009否 2012是 2000是 1900否
# 根据你输入的年份,判断是否为闰年?

# year=int(input("请输入一个年份:"))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print("%s年是闰年!"%year)
# else:
#     print("%s年不是闰年!"%year)
#
# if year%400==0:
#     print("闰年")
# else:
#     if year%4==0 and year%100!=0:
#         print("闰年")
#     else:
#         print("非闰年")


while True:
    try:
        s = int(input('请输入一个数字：'))
        tlist=[]
        s=s**2
        if s<=100:
            tlist.append(s)
            print('输入值小于100，已添加到列表')
        else:
            print('输入值大于100，已退出程序')
            break
    except:
        print('输入类型有误，请重新输入！')


