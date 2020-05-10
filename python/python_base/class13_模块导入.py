# import keyword
# print(keyword.kwlist)

# import math# 引入模块去调用模块中的功能(对象)
# print('圆周率:',math.pi)
# print('正弦:',math.sin(100))
# print('余弦:',math.cos(100))

# # 导入模块的几种方式
# # 第1种方式
# import math# 导入一个模块
# import math,re,random,time# 导入多个模块
# print(math.pi)

# 第2种方式
# from math import pi,sin,cos
# from math import *# 容易造成对象的覆盖
# 1.导入指定的对象
# 2.书写更加方便
# print("圆周率:",pi)
# print(sin(100))
# print(cos(100))

# 第3种方式
# import random as rm# 起别名
# import numpy as np# 起别名
# import pandas as pd
# print(rm.random())

# # 导入自己编写的模块
# import my_function as mf
# print(mf.jc(5))
# mf.print_num(100)
# print(mf.word)

# 不同层级目录下模块的导入
# import new_f.my_func

# 任意路径下模块导入
import sys
# print(sys.path)# 检索的路径目录
# sys.path.append("F:\\Bin\\3rd")
# print(sys.path)# 手动添加文件路径
# import my_func






