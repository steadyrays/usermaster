# os模块
# os.sep:取代操作系统特定的路径分隔符
# os.getcwd:得到当前工作目录，即当前python脚本工作的目录路径。
# os.getenv()和os.putenv:分别用来读取和设置环境变量
# os.listdir():返回指定目录下的所有文件和目录名
# os.remove(file):删除一个文件
# os.stat（file）:获得文件属性
# os.mkdir(name):创建目录
# os.rmdir(name):删除目录
# os.exit():终止当前进程
# os.path.split():返回一个路径的目录名和文件名
# os.path.isdir(name):判断name是不是目录，不是目录就返回false
# os.path.exists(name):判断是否存在文件或目录name
# os.path.abspath(name):获得绝对路径
# os.path.isabs():判断是否为绝对路径
# os.path.join(path,name):连接目录与文件名或目录
# os.path.basename(path):返回文件名
# os.path.dirname(path):返回文件路径
import os
# 1、os.getcwd() os.chdir()
# print("获取当前的工作路径:",os.getcwd())
# os.chdir(r"D:\cs2433_文件迁移\桌面\excel&csv")# 修改当前工作目录
# print("获取当前的工作路径:",os.getcwd())
# with open("泰坦尼克号.csv")as f:
#     print(f.read())

# 2、os.listdir() 获取目录下的所有文件信息
import re
# dir=os.listdir(r"E:\class06_python\作业\第03天")
# print(dir)
# for name in dir:
#     print(re.search("_(\w+)\.",name).group(1))

# 3、os.mkdir()创建文件夹 os.rmdir()删除文件夹 os.remove()删除文件
# for i in range(100):
    # os.mkdir(r"E:\class06_python\OS模块\文件夹%s"%i)

# os.rmdir(r"E:\class06_python\OS模块\新建文件夹")

# os.remove(r"E:\class06_python\OS模块\新建文本文档.txt")

# 4、os.path.exists()
# 判断文件夹是否存在
# print(os.path.exists(r"E:\class06_python\OS模块\新建文件夹"))
# 在创建文件之前先进行判断是否存在,如果存在就不创建,如果不存在创建一个新的文件
# path="E:\class06_python\OS模块\文件夹-1"
# if os.path.exists(path):
#     print("文件已存在!")
# else:
#     os.mkdir(path)

# 5、os.walk()游走函数

walk=os.walk("E:\class06_python\作业")
# print(list(walk))
for i in walk:
    print(i)
    print("* "*50)
    print()


'abcdefghijklmno'




