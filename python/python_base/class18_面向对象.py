# 创建类
# class 类名:
#     pass

# class Car:# 类名要符合我们的标识符命名规则,一般遵从驼峰命名法
#     pass
# print(Car)#  <class '__main__.Car'>
# c=Car()# 创建一个对象
# print(c,type(c))
# print(type('abc'),type([1,2,3]))

class Car:
    # 移动
    def move(self):# 实例方法
        print("车在马路上奔跑...")
    # 鸣笛
    def toot(self):
        print("车在鸣笛...嘟嘟嘟...")

bwm=Car()
# # 对象.方法(参数)
# bwm.move()
# bwm.toot()
# bwm.color='红色'
# print("车的颜色是%s!"%bwm.color)# 添加属性
# bwm.color='黄色'
# print("车的颜色是%s!"%bwm.color)# 修改属性


# # 构造函数__init__()
# class Car:
#     def __init__(self,name="小黑车",color="黑色"):# 对象初始化
#         self.name=name
#         self.color=color
#         self.password='123456'
#     # 移动
#     def move(self):# 实例方法
#         print("我的%s在马路上奔跑..."%self.name)
#         self.toot()
#     # 鸣笛
#     def toot(self):
#         print("车在鸣笛...嘟嘟嘟...")
#     def change_color(self,new_color):
#         self.color=new_color
#         print("已经将汽车的颜色修改为%s!"%self.color)
#     def get_key(self):
#         return self.password
# # bmw=Car("宝马7系")# 产生一个实例化对象
# # print("我买的第一辆车名字是:%s"%(bmw.name))
# # bc=Car("奔驰八系","白色")# 产生一个实例化对象
# # print("我买的第二辆车名字是:%s"%(bc.name))
# # bc.move()# 实例属性和实例方法是共享的
# # print(bc.color)
# # bc.change_color("红色")

# bc=Car()# 产生一个实例化对象
# print("我买的第二辆车名字是:%s"%(bc.name))
# bc.move()# 实例属性和实例方法是共享的
# print(bc.color)
# bc.change_color("红色")
# print(bc.get_key())


# 面向对象三大特性
# 封装
# 隐藏我们对象的属性和实现的细节,只提供必要的方法

# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age# 私有属性
#     def eat(self):
#         print("%s你都已经%s岁了,还在吃零食!"%(self.name,self.__age))
#     def __say_hi(self):
#         print("偷偷告诉你是白雪公主!")
# p=People("白雪",20)
# p.eat()
# p.say_hi()
# print(p.age)
# print(p._People__age)# 从外部直接调用私有属性
# p._People__say_hi()# 私有属性和方法主要是为了防止不小心修改重要的属性和方法

# 继承
# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self):
#         print("吃饭!")
#     def sleep(self):
#         print("睡觉!")
# class Chinese(People):
#     def __init__(self,name,age,hob):
#         People.__init__(self,name,age)
#         self.hob=hob


# class RiBenRen(People):
#     pass
# c=Chinese("小明",15,"打游戏")
# # r=RiBenRen()
# c.sleep()
# print(c.name,c.age,c.hob)

# 多继承
class A:
    def say_a(self):
        print("我是A类方法")
class B(A):
    def say_b(self):
        print("我是B类方法")
class C(B):
    def say_c(self):
        print("我是C类方法")
# c=C()
# c.say_c()
# c.say_b()
# c.say_a()

# class A:
#     def say(self):
#         print("我是A类方法")
# class B:
#     def say(self):
#         print("我是B类方法")
# class C(B,A):# 从左向右进行继承
#     def say_c(self):
#         print("我是C类方法")
# c=C()
# c.say_c()
# c.say()

# 多态
# 不同的对象调用相同的方法结果不同
class People:
    def eat(self):
        print("吃饭")
class Chinese(People):
    def eat(self):
        print("吃水稻,吃小麦!")
class Japanese(People):
    def eat(self):
        print("吃寿司,吃生鱼片!")
class Indian(People):
    def eat(self):
        print("吃飞饼,吃咖喱!")
c=Chinese()
j=Japanese()
i=Indian()
c.eat()# 方法的重写
j.eat()
i.eat()

# alist=[1,2,3]
# print(dir(alist))
# print(alist.__add__([4,5,6]))
# print([1,2,3]+[4,5,6])
# print(alist.__mul__(3))
# print(alist*3)
# print(alist.__len__())
# print(len(alist))
# print(dir('abc'))
# print(dir({'a':1}))
























