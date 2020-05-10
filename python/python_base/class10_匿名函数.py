# 匿名函数
# 结构
# f=lambda 参数:输出的结果
# a=10
# f=lambda x:x**2
# print(f)
# print(f(a))
# f=lambda :'hello world'
# print(f())
# f=lambda x,y,z:x+y+z
# print(f(10,20,30))

# 列表推导式
# 生成一个1-100之间的整数列表
# num=[]
# for i in range(1,101):
#     num.append(i)
# print(num)
# print(list(range(1,101)))

# l1=[i for i in range(1,101)]
# print(l1)
# l2=[i*i for i in range(1,101)]
# print(l2)
# l3=[i.upper() for i in 'abc']
# print(l3)
# # 生成一个1-100之间的整数列表,元素类型为字符串
# num=[1,2,3,4,5,6]
# r=[str(i) for i in num]
# print(','.join(r))
# l4=[i for i in range(1,101) if i%3==0]
# print(l4)

# 其他生成式
# print([i for i in range(10)])# 列表生成式
# print((i for i in range(10)))# 生成器
# string='abcabefgabfg'
# print({i:string.count(i) for i in 'abcabefgabfg'})# 字典生成式
# print({i:10 for i in 'abcabefgabfg'})# 字典生成式
# print({i for i in 'abcabefgabfg'})# 集合生成式

# lambda表示一个函数，输入1-100的整数列表，返回可以整除三的元素列表
# inp=[i for i in range(1,11)]
# oup=[i for i in range(1,101) if i%3==0]
# print(inp)
# print(oup)
# f=lambda x:[i for i in x if i%3==0]
# print(f(inp))

