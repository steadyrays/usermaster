# 可迭代对象:可以循环访问的对象

# 迭代器
# l=['a','b','c','d','e',10000000]
# for i in range(len(l)):
#     print("处理第%s个数据:%s"%(i+1,l[i]))
# iter_l=iter(l)# 转换成迭代器
# next()函数访问迭代器中的元素
# print(next(iter_l))
# print(next(iter_l))
# print(next(iter_l))
# print(next(iter_l))
# print(next(iter_l))
# print(next(iter_l))
# print(next(iter_l))
# for i in iter_l:
#     print("处理数据:%s"%i)
# 知识点:迭代器每次只生成一个目标

# n=[1,2,3,4,5,6]
# def f(data):
#     if data%2==0:
#         return True
#     else:
#         return False
# ft=list(filter(f,n))
# print(ft)

# print('-----第一次访问迭代器-----')
# for i in ft:
#     print(i)
# print('-----第二次访问迭代器-----')
# for i in ft:
#     print(i)
# 知识点:迭代器的元素只能访问一次


# 生成器
# def f1():
#     print("第1次暂停")
#     yield '第1次访问返回的结果'# yield 暂停函数的调用,返回一个结果
#     print("第2次暂停")
#     yield '第2次访问返回的结果'
#     return 100 # reutrun结束函数的调用
# r=f1()
# print(r)
# print(next(r))
# print(next(r))
# for i in r:
#     print(i)

# a=[1,2,3,4,5,6]
# def f1(tlist):
#     l=[]
#     for i in tlist:
#        l.append(i**2)
#     return l
# for i in f1(a):
#     print(i)
#
# print("-"*100)
#
# a=[1,2,3,4,5,6]
# def f2(tlist):
#     for i in tlist:
#         yield i**2# 优点:更加节省内存空间  缺点:速度相对较慢
# for i in f2(a):
#     print(i)






