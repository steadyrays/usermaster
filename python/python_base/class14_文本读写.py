# txt / csv / excel / word

# open函数
# open(name="文件路径",mode="模式",encoding="编码")
# path="C:\\Users\\ibf\\Desktop\\工程品管 IDL 门禁记录.txt"
# f=open(path,encoding='utf-8')# 打开文件
# print(f.read())# 读取全部文本信息
# f.close()# 关闭文件连接# unicode utf-8 gbk

# 绝对路径
# path1="C:\\Users\\ibf\\Desktop\\工程品管 IDL 门禁记录.txt"
# path2=r'C:\Users\ibf\Desktop\工程品管 IDL 门禁记录.txt'
# path3='C:/Users/ibf/Desktop/工程品管 IDL 门禁记录.txt'
# f=open(path3,encoding='utf-8')# 打开文件
# print(f.read())# 读取全部文本信息
# f.close()# 关闭文件连接# unicode utf-8 gbk

# 相对路径
# f=open("文本文件.txt",encoding='UTF-8')# 当前目录
# f=open("./文本文件.txt",encoding='UTF-8')# 当前目录
# f=open("../文本文件.txt",encoding='UTF-8')# 上级目录
# print(f.read())
# f.close()
# os模块 os.chdir()

# 常用文件操作模式
# read r  write w  append a
# 读取模式read
# f=open("文本文件.txt",'r',encoding='UTF-8')# 当前目录
# print(f.read())# 读取整个文本的信息,返回字符串
# print(f.read(10))# 读取10个字符
# print(f.readline())# 读取第一行的文本信息
# print(f.readlines())# 读取所有行的文本信息,返回列表
# text=f.read()
# print(text)
# f.seek(0)# 移动指针位置
# print(f.readlines())
# f.close()


# 写入模式write
# 每次write模式打开文件时,会清空文本内容
# f.write(字符串)
# 当目标路径的文件不存在时会新建
# f=open("文本文件.txt",'w',encoding='UTF-8')
# f.write('123abc'+'\n')
# f.write('123abc'+'\n')
# f.write('123abc'+'\n')
# f.write('123abc'+'\n')
# f.close()

# 练习1
l=['小明','小张','小李','小黑']# 写入csv中
# 方法1
# f=open("文本文件.csv",'w',encoding='UTF-8')
# f.write(','.join(l))
# f.close()

# 方法2
# f=open("文本文件.csv",'w',encoding='UTF-8')
# for i in l:
#     f.write(i+',')
# f.close()

# 练习2
# 方法1
info=[# 写入csv中
    ['姓名','语文','数学','英语'],
    ['小A','90','80','92'],
    ['小B','80','98','78'],
    ['小C','91','95','94'],
    ['小D','47','55','61'],
    ['小E','77','82','90']
]
f=open("课程成绩.csv",'w',encoding='UTF-8')
for i in range(6):
    f.write(','.join(info[i]))
    f.write('\n')
f.close()

# 方法2
# f=open("课程成绩.csv",'w',encoding='UTF-8')
# for line in info:
#     for word in line:
#         f.write(word+',')
#     f.write('\n')
# f.close()

# 追加模式append(在文件末尾追加信息)
# f=open("课程成绩.csv",'a',encoding='UTF-8')
# f.write('小F,100,100,100,')
# f.close()

# 混合模式(可读可写)
# r+ w+ a+
# f=open("课程成绩.csv",'r+',encoding='UTF-8')
# f.write('acb')
# f.seek(0)
# print(f.read())
# f.close()

# rb wb bite比特 字节流
# 主要用于处理图片、视频、音频的信息

# with文件管理器(无需关闭文件信息)
# with open("课程成绩.csv",'r',encoding='UTF-8')as file:
#     print(file.read())

# 想一想:
# 怎么将一个标准的txt文件变成csv文件



string="人生苦短,我用Python。"
print(string+' Oh yeah!',end=' 123 ')





