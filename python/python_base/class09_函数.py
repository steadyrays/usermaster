# 定义函数:
# def 函数名(参数1,参数2,...):
#     """函数功能的描述"""
#     函数体(代码块)

# 创建函数
# def say_hi():# 函数名要符合标识符命名规则
#     """给大家拜个早年!"""
#     print("恭喜发财,红包xxx!")
#     print("初次见面请多关照!")
# # a=100
# # print(a)
# say_hi()

# # 位置参数
# def say_hi(name1,name2):# 形参
#     """给大家问个好"""
#     print("大家好,我叫{},喜欢骂娘!".format(name1))
#     print("你们好,我是{},喜欢打篮球。".format(name2))
#
# say_hi("李云龙","蔡徐坤")# 实参

# 关键词参数
# def shout(dog,cat):
#     print(dog+":汪汪汪!")
#     print(cat+":喵喵喵!")
# shout(dog="汪星人",cat="喵星人")
# shout(cat="喵星人",dog="汪星人")


# print(123,sep=' ',end=' ')
# print(123)
#sep和end的用法
# print("hello","python",sep="")
# print("hello","python",sep=" ")
# print("hello","python",end="")
# print("hello","python")
#默认为end=('\n')换行
#sep默认为空格

# 默认值参数

# def num(a,b,c=100,d=200):
#     print(a,b,c,d)
# num(10,20,30,40)
# num(10,20,30)
# num(10,20)

# 可变参数
# def f1(a,b,*c):# *args
#     print(a,b)
#     print("-"*50)
#     print(c)# 元组
# f1(1,2,3,4,5)
# parm=[3,4,5]
# f1(1,2,*parm)

# def f2(a,b,**c):# **kwargs
#     print(a, b)
#     print("-" * 50)
#     print(c)  #字典类型
# f2(1,2,name='李云龙',age='50',hob='吹牛')
# parm={'name': '李云龙', 'age': '50', 'hob': '吹牛'}
# f2(1,2,**parm)


# return 和 print
# def add(a,b):
#     print(a+b)
#     return a+b# 函数调用结束后返回什么信息
#     # print(a+b)# return语句执行后函数调用结束
# def mul(a,b):
#     print(a*b)
#     return a*b
# num1=100
# num2=200
# add(num1,num2)
# mul(num1,num2)
# print(add(num1,num2))
# print(mul(num1,num2))

# tlist=[1,2,3,4]
# tlist.append(1)
# print(tlist)
# print(tlist.append(1))
# print(tlist.pop())


# 定义一个函数,输入一个正整数,求1到这个整数的累加和
# 5-->1+2+3+4+5
# 6-->1+2+3+4+5+6
# def add_number(n):
#     s=0
#     for i in range(1,n+1):
#         s=s+i
#     return s
# print(add_number(5))

# 求n的阶乘
# 5!=1*2*3*4*5
def jc(n):
    s = 1
    for i in range(1,n+1):
        s=s*i
    return s

# print(jc(365))

def jn(m):
    t = 1
    for i in range(1,m+1):
        t=t*i
    return t

# print(jn(365-20))

# print(jn(345)/jc(365))

# 求1-n之间所有整数的阶乘
# 1!+2!+3!+4!+...+n!
# def jc_add(n):
#     s=0
#     for i in range(1,n+1):
#         s=s+jc(i)
#     return s
# print(jc_add(5))

# def jc_add(n):
#     s=0
#     for i in range(1,n+1):
#         h=1
#         for j in range(1,i+1):
#             h=h*j
#         s+=h
#     return s
# print(jc_add(5))



# 参数的传递
# a=10000
# def f(n):
    # n=20000# 局部环境无法修改全局环境
    # print(id(n))
    # print(n)
# print(id(a))
# f(a)
# print(a)
# print(id(a))

# a=[1,2,3]
# def f(n):
#     n.append(4)# 可变类型在函数中可以修改
#     print(n)
#     print(id(n))
# print(id(a))
# f(a)
# print(a)
# print(id(a))

# a=[1,2,3]
# def f(n):
#     n=[4,5,6]# 所有函数内创建的变量值作用于函数环境下,对全局环境没有影响
#     print(n)
#     print(id(n))
# print(id(a))
# f(a)
# print(a)
# print(id(a))

# a=10
# b=20
# def f():# 局部环境可以调用全局环境
#     global a# 将a修改到全局环境中
#     a=1
#     b=2# 局部变量无法影响全局变量
#     print(a)
#     print(b)
# f()
# print(a,b)

# python的参数传递是引用传递
# 1、函数内可以调用全局环境中的变量
# 2、局部环境无法影响全局环境(global可以实现全局环境对象的修改)
# 3、可变对象在函数中能被修改

# 5!=5*4*3*2*1
# def f(n):
#     if n==1:
#         return 1
#     else:
#         return n*f(n-1)
# print(f(5))
# 5！=5*4!=5*4*3*2*1!

# 斐波那契数列
# 1 1 2 3 5 8 13 21 34 55....
# def f(n):
#     if n==1 or n==2:
#         return 1
#     return f(n-1)+f(n-2)
# print(f(6))
