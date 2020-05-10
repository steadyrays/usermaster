# # 字符串方法
# t=[1,2,3]
# t.append(4)
# print(t)
# 对象.方法(参数)
# string='abc123.!@#$a'

# 1、find方法
# ''.find(sub,start,end)
# print(string.find('a'))# 返回元素首次出现的索引位置
# print(string.find('123'))
# print(string.find('z'))# 查找不到的元素返回-1
# print(string.find('1',4,9))# start-end控制查找范围

# # 请输入一个信息,并且判断是否存在于string中
# word=input("请输入一个字符信息:")
# if string.find(word)==-1:# word in string
#     print("string中不包含此信息!")
# else:
#     print("string中包含此信息!")
info=['美国-华盛顿','俄罗斯-列宁格勒','中国-北京','苏格兰-xxx']
# 用find方法打印出所有城市信息

# # 2、join(将一个可迭代对象转字符串的方法)
# # list(str)
# # tuple(str)
# print(''.join(['a','b','c']))
# print('-'.join({'a':1,'b':2,'c':3}))
# print('**'.join('abc'))
# print(' '.join(('a','b','c')))
# print(','.join(['a','b','c']))
# # print(','.join([1,2,3]))# 元素必须为字符串类型
# loc=('上海','浦东','世纪大道')
# p1='**'.join(loc)
# print(p1)

# # 3、split() 分割(类似于join的逆方法,返回的是列表)
# print(p1.split("**"))
# print(p1.split("*"))
# print(p1.split("**",1))# 设置最大分割次数

# word='上海 浦东-世纪大道'
# result=['上海', '浦东', '世纪大道']
# r1=word.split()[0]
# r2=word.split()[1].split('-')
# r2.insert(0,r1)
# print(r2)

# # 4、strip()去除前后的指定字符串
# string='    北京故宫    '
# print(string)
# print(len(string))
# print(string.strip())
# print(len(string.strip()))

# 指定字符信息
# string='----巴黎圣母院----'
# print(string.strip('-'))
# string='----巴黎圣-母院-+---'
# print(string.strip('-'))

# # 5、replace()替换指定字符信息
# string='----上海东方明珠----'
# print(string.replace('-',''))
# string='----上海东-方明珠--+--'
# print(string.replace('-',''))
# string='----上海东方明珠----'
# print(string.replace('-','+',4))# count控制替换次数

# word='上海 浦东-世纪大道'
# print(word.replace('-',' ').split())

# # 练习
# strip_string="-----巴黎圣母院++++++"
# print(strip_string.strip('+').strip('-'))
#
# info=['美国-华盛顿','俄罗斯-列宁格勒','中国-北京','苏格兰-xxx']
# # 用find方法打印出所有城市信息
# for i in info:
#     print(i.split('-')[1])
#     print(i[i.find('-')+1:])

# 其他字符串方法

# s1='IBEIFENG'
# print(s1.isupper())# 判断字符串元素是否都是大写
# s2='ibeifeng'
# print(s2.islower())# 判断字符串元素是否都是小写
# print(s2.upper())# 将字符元素都变成大写
# print(s1.lower())# 将字符元素都变成小写
#
# s3='abc'
# print(s3.isalpha())# 判断字符元素是否都是字母、中文
# print(s3.isalnum())# 判断字符元素是否都是字母或数字、中文
# print(s3.isdigit())# 判断字符元素是否都是数字
# print(s3.isspace())# 判断字符元素是否是空格信息 #  \t \n
# print(s3.istitle())# 判断是否首个元素是大写字母
#
# print(isinstance(s3,str))# 类型判断
# print(isinstance(s3,list))
#
# print(s3.startswith('ab'))# 是否以某个字符开始
# print(s3.endswith('bc'))# 是否以某个字符结束

# 7、format(格式化字符串方法)
# print("我叫%s,今年%s岁"%('小明',13))
# print("我叫{},今年{}岁".format('小明',13))
# print("我叫{0},今年{1}岁。欢迎你{0}同学!".format('小明',13))
# print("我叫{name},今年{age}岁".format(age=13,name='小明'))
# format函数的其他功能







