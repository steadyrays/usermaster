# 注释符(pycharm ctrl+/ 快速注释和取消注释)
# print("hello world!1")
# print(123)# print("hello world!2")
# print("hello world!3")
# print("hello world!4")
# print("hello world!5")

# 三引号用于创建多行字符串,有时也做注释
"""
第一行注释
第二行注释
第三行注释
第四行注释
"""

# 转义

# 输入和输出
# string="人生苦短,我用Python。"
# # end输出结束后打印的字符,默认换行符
# print(string+' Oh yeah!',end='---------')
# print(string+' Oh yeah!',end='\n')

# string1="人生苦短"
# string2="我用Python"
# sep打印多个对象时字符之间的分隔符,默认空格
# print(string1,string2,1,2,sep='++')

# 输入(接受信息都为字符串类型)
# name=input("请输入你的姓名:")
# age=input("请输入你的年龄:")
# print(type(name),type(age))
# print("你的名字是:",name)
# print("你的年龄是:",age)

# 请输入你的名字和年龄,并且打印出你的名字和明年的年龄
# 要求:一条print语句完成
# name=input("请输入你的姓名:")
# age=input("请输入你的年龄:")
# print("你的名字是"+name+"你的年龄是"+str(int(age)+1)+"岁")
# print("你的名字是"+name+"你的年龄是",int(age)+1,"岁",sep="")

# 字符串格式化
# 创建字符串模板,常用与创建自定义的字符串
# print('今天学习的课程是%s'%'python编程基础')
# print('今天学习的课程是%s'%'python基础')
# print('我的名字是%s，今年%d岁,体重是%.1f公斤'%('程时',18,72.5))
# name=input("请输入你的名字:")
# age=input("请输入你的年龄:")
# weight=input("请输入你的体重:")
# print('我的名字是%s，今年%s岁,体重是%s公斤'%(name,age,weight))

# 1、输入一串字符，并返回它的长度。（结合input用法）
# string=input("请输入一段字符信息:")
# print("输入的字符信息长度是%s"%len(string))

# 2、输入你的名字和年龄，输出你明年是多少岁（结合input和字符串格式化）
# name=input("请输入你的名字:")
# age=input("请输入你的年龄:")
# print("你的名字是%s,你的年龄是%d岁,你明年%d岁"%(name,int(age),int(age)+1))
# print("你的名字是%s,你的年龄是%s岁,你明年%s岁"%(name,age,int(age)+1))

