# while循环
# while 条件表达式:
#     语句块1
#     语句块2
#     语句块3
#     ....
# # 每次执行while子语句之前进行条件表达式的判断,如果为True则执行,不断重复直到,条件为False时停止
# print("---------while循环语句开始--------")
# i=1
# while i<=100:
#     print("我要减肥!")
#     i+=1# i=i+1
# print("---------while循环语句结束--------")

# print("---------while循环语句开始--------")
# i=1# 起始值
# while i<=100:# 结束条件
#     print("我要减肥第%s遍!"%i)# 循环语句
#     i+=1# i=i+1# 步长,让条件趋近于结束
# print("---------while循环语句结束--------")

# 破冰行动 48

# print("---------while循环语句开始--------")
# i=1# 起始值
# while i<=48:# 结束条件
#     print("我正在看《破冰行动》第%s集!"%i)# 循环语句
#     i+=1# i=i+1# 步长,让条件趋近于结束
# print("终于看完,可以睡觉了 =-= !!")
# print("---------while循环语句结束--------")

# 练习1:求1-100的累计和
# 0+1+2+3+4+5+...+99+100

# i=1
# s=0
# while i<=100:
#     s=s+i
#     i+=1
# print(s)

# 练习2:求1-100之间偶数的累计和
# 0+2+4+6+8+10+...+98+100

# 方法1
# i=1
# s=0
# while i<=50:
#     s=s+2*i# 1 2 3 4 5 ... 50
#     i+=1
# print(s)
#
# i=0
# s=0
# while i<50:#2 4 6 8 100
#     s=s+i+(i+2)#0 1 2 3 4 5 ... 49
#     # print(i)
#     i+=1
# print(s)

# # 方法2
# i=2
# s=0
# while i<=100:
#     s=s+i
#     # print(i)
#     i+=2
# print(s)

# # 方法3
# i=1
# s=0
# while i<=100:
#     # print(i)
#     if i%2==0:
#         s=s+i
#     i+=1
# print(s)


# print("* ")
# print("* * ")
# print("* * * ")
# print("* * * * ")
# print("* * * * *")
# print("* * * * ")
# print("* * * ")
# print("* * ")
# print("* ")
i=1
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 4 3 2 1

# while i<=9:
#     if i<=5:
#         print("* "*i)#
#     else:# 6 4 7 3 8 2 9 1
#         print("* "*(10-i))
#     i+=1

# while i<=9:
#     print("* "*(-abs(i-5)+5))
#     i+=1

# 作业:
# 如何删除字典中的键值对
# dict.pop(key)

# 如何合并两个字典中的信息
# dict1.update(dict2)

# 用循环求5!=5*4*3*2*1
# 1*1*2*3*4*5
# 0+1+2+3+4+5
# i=1
# s=1
# while i<=5:
#     s=s*i
#     i+=1
# print(s)

# info=[{"name":"小明","age":22,"job_info":{"jobname":"程序员","salary":"10000"},"city":"北京"},
#       {"name":"老王","age":40,"job_info":{"jobname":"工程师","salary":"15000"},"city":"上海"},
#       {"name":"老张","age":42,"job_info":{"jobname":"医生","salary":"20000"},"city":"深圳"}]
# 通过格式化字符串用以下格式打印输出小明、老王、老张的信息：
# xxx的职业是xxx,目前xxx岁,在xxx工作每个月能拿xxxx元。
# 例如结果是print('小明的职业是程序员,目前22岁,在北京工作每个月能拿10000')
# 利用循环将三个信息打印出来
# print(info[0]['name'],info[0]['job_info']['jobname'],info[0]['age'],info[0]['city'],info[0]['job_info']['salary'])
# print("%s的职业是%s,目前%s岁,在%s工作月收入为%s元"%(info[0]["name"],info[0]["job_info"]["jobname"],info[0]["age"],info[0]["city"],info[0]["job_info"]["salary"]))
# print("%s的职业是%s,目前%s岁,在%s工作月收入为%s元"%(info[1]["name"],info[1]["job_info"]["jobname"],info[1]["age"],info[1]["city"],info[1]["job_info"]["salary"]))
# print("%s的职业是%s,目前%s岁,在%s工作月收入为%s元"%(info[2]["name"],info[2]["job_info"]["jobname"],info[2]["age"],info[2]["city"],info[2]["job_info"]["salary"]))
#
# i=0
# while i<=2:
#     print("%s的职业是%s,目前%s岁,在%s工作月收入为%s元"%
#           (info[i]["name"],info[i]["job_info"]["jobname"],info[i]["age"],info[i]["city"],info[i]["job_info"]["salary"]))
#     i+=1

# # 求解
# 5!+4!+3!+2!+1!
# 0+1+2+3+4+5
# # 0+1！+2！+3！+4!+5!#+6!+...+99!+100!
# i=1
# s=0
# while i<=6:
#     # i-->i!将i变成i的阶乘
#     j=1
#     h=1
#     while j<=i:
#         h=h*j
#         j+=1
#     # i-->i!将i变成i的阶乘
#     print('当前i的值为%s,它的阶乘是%s'%(i,h))  # i的阶乘
#     s=s+h
#     i+=1
# print(s)

# 用循环求5!=5*4*3*2*1
# 1*1*2*3*4*5
# 0+1+2+3+4+5
# i=1
# s=1
# while i<=3:
#     s=s*i
#     i+=1
# print(s)
# i-->i!
# j = 1
# h = 1
# while j <= 5:
#     h = h * j
#     j += 1
# print(h)# i的阶乘






