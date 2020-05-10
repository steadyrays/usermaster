import re
# 3种常用匹配模式
# 常见匹配方法
# # 1、re.match(pattern,string)# 从目标字符串的开始进行匹配,
# pattern='abc'
# string='abcddddddefg123 python_3.5123abc'
# result=re.match(pattern,string)
# print(result) #左闭右开
# print(result.span())#找到匹配信息的所在位置
# print(result.group())#找到匹配的信息

# # 2、re.search(pattern,string)
# pattern='123'
# string='abcddddddefg123 python_3.5123abc'
# result=re.search(pattern,string)
# print(result)
# print(result.span())
# print(result.group())

# # 3、re.findall(pattern,string)
# string='abcddddddefg123Python_3.5123abc'
# pattern='Python'
# result=re.findall(pattern,string)# 匹配所有符合规则的元素,返回列表
# print(result)

# 一：原子
# 普通字符串作原子
# pattern='baidu'
# string='http://www.baidu.com/'
# result=re.search(pattern,string)
# print(result)

# # 非打印字符作原子
# pattern='\n'# \t
# string='''
# http://www.baidu.com/
# http://www.baidu.com/
# '''
# result=re.findall(pattern,string)
# print(result)

# 通用字符作原子
# 通用字符做原子
# \d匹配数值字符 0-9 \D 取反#
# \w匹配字母数字中文下划线 \W 取反
# \s匹配空白字符 \S 取反
# .（点）#匹配除了换行符外所有字符
# pattern='.'
# string='abcdefg123 PYTHON_3.5 ? # % 中文 \n \t'
# result=re.findall(pattern,string)
# print(result)

# pattern='....python....'
# string='abcdefg123 python_3.5'
# result=re.search(pattern,string)
# print(result)

# # 原子表
# pattern='[^0-9a-zA-Z\W_]'#[a-zA-Z0-9] [^\w\s] [一二三四五六七八九十]
# pattern=r'[\u4e00-\u9fa5]'
# string='ybcdefg123 Python_3.5 a R $ % ! 一二三四五六七八九十'
# result=re.findall(pattern,string)
# print(result)

# 二：元字符

# 边界限定元字符
# pattern1='abc$'#结束限定符
# pattern2='^123'#开始限定符
# string='123defg 123python_abc_3.5abc'
# # print(re.search(pattern1,string))
# print(re.findall(pattern1,string))
# print(re.findall(pattern2,string))

# 次数限定元字符
# * ? +{n} {n,} {n,m}
# * 重复前面一个字符0~无穷次
# + 重复前面一个字符1~无穷次
# ? 重复前面0-1次
# {n}重复n次 {n,}重复n次到无穷次 {n,m}重复n次到m次

# pattern1='abcd*'
# # pattern1='[a-z]*'
# pattern2='abcd+'
# pattern3='abcd?'
# pattern4='abcd{2}'
# pattern5='abcd{2,}'
# pattern6='abcd{2,4}'
# pattern7='p[a-z]{5}'
# string='abcddddddefg123 python_3.5abc'
# print(re.search(pattern1,string))
# print(re.search(pattern2,string))
# print(re.search(pattern3,string))
# print(re.search(pattern4,string))
# print(re.search(pattern5,string))
# print(re.search(pattern6,string))
# print(re.search(pattern7,string))

# 模式选择符

# pattern='python|php|abc'
# string1='abcdefg123 python_3.5abc'
# string2='abcdefg123 php_3.5abc'
# print(re.findall(pattern,string1))
# print(re.findall(pattern,string2))


# 模式单元符

# pattern='<(.*?):(.*?)>'#  ?懒惰模式
# string='<吕布:你好> <吕小布:大噶好123?> <川普:sdasfsfddgegst.....>'
# result=re.findall(pattern,string)
# print(result)
# pattern='(cd)+'#  (\w{6})(\d.\d)_
# string='abcdcdcdcdefg123 python3.5_php_3.5abc'
# result=re.search(pattern,string)
# print(result.group())



# # 贪婪模式和懒惰模式(在符合规则的情况下尽量少的匹配)
# pattern='\w+?'#\w+
# string='abcddddddefg123 python_3.5123abc'
# result=re.search(pattern,string)
# print(result)

# compile和re.S模式

# string='abcddddddefg123\npython_3.5123ABC'
# pattern1=re.compile('abc',re.S)# re.S#让点号.能够匹配换行符 re.I#忽略大小写
# print(re.findall(pattern1,string))
# pattern2=re.compile('abc',re.I) #忽略大小写
# print(re.findall(pattern2,string))


# re.split()指定匹配字符进行分割
# re.split()
# string='a1b2c3d4'
# pattern='[0-9]'
# result=re.split(pattern,string) # maxsplit指定次数

# print(result)
# print('a b   c'.split(' '))
# print(re.split('\s+', 'a b   c'))

# re.sub()指定匹配字符进行替换
# re.sub
# string='a1pythonb2c3d4cython'
# pattern='[cp]ython'
# result=re.sub(pattern,'PHP',string)# count控制次数
# print(result)

# phone=input('请输入电话号码：')

# phone=input('请输入电话号码：')
# 判断电话号码格式是否正确
# 长度11 1 160
# if len(phone)==11 and phone[0]=='1' and phone[1] not in '160' and phone[1:].isdigit():
#     print("输入电话号码格式正确!")
# else:
#     print("输入电话号码格式不正确!")

# if re.search("^1[2345789]\d{9}$",phone):# match对象 None
#     print("输入电话号码格式正确!%s"%phone)
# else:
#     print("输入电话号码格式不正确!")

# 判断用户输入密码的问题
# 8-12 密码字符只能是字母和数字 至少包含一个大写字母

# password=input('请输入密码：')
#
# if re.search('^[a-zA-Z0-9]{8,12}$',password) and re.search('[A-Z]',password):
#     print('密码正确')
# else:
#     print('密码错误')


# s='name:小明 age:12,name:小汪 age:3,name:小李飞刀 age:18'
# print(re.findall('name:(\w+) age:(\d+)',s))


# # 作业
# a="二狗 59分"# 用re.sub将59替换成100


# tels=[13100008724,15898030575,13776814997,18915089373,18917210234,20000,342422199802021448]
# # 匹配不是以4和7结尾的手机号

# 用正则表达式将字符串中的字母数字符号清除掉,最终结果为"北风网 上海"
# string="abcdefg 北风网 上海 404 not found"

# 张无忌 赵敏 周芷若 小昭 张三丰 杨逍 玄冥二老

#技能分析

import re

#读取文本内容
f=open('51job岗位信息.txt','r',encoding='utf-8')
text=f.read()
f.close()
pattern=re.compile('[a-zA-Z]+')
skill_list=re.findall(pattern,text)
print(skill_list)
skill_list=()





