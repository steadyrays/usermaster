import pymysql# 第三方模块
# cmd下执行代码(安装): pip install 模块名
# cmd下执行代码(卸载): pip uninstall 模块名
# pip3 install 模块名 conda install 模块名

conn=pymysql.connect(host="localhost",# ip地址
                user="root",# 用户名
                password="123456",# 登录密码
                db="class_06",# 连接数据库名
                charset="utf8",# 数据库编码
                port=3306)# 端口号
# 打印连接
# print(conn)

# 创建游标
cursor=conn.cursor()

# # 1、创建数据库
# create_sql="""create table if not exists
# student(studentName varchar(255) not null,age int(10) not null)"""
# cursor.execute(create_sql)# 执行sql命名
# conn.commit()# 提交事务

# # 2、插入数据
# 基础数据插入方式
# insert_sql="insert into student values('小明',18)"
# cursor.execute(insert_sql)# 插入一条数据
# conn.commit()# 提交事务
# 格式化字符传递信息
# insert_sql="insert into student values(%s,%s)"
# parm=('老王',33)
# cursor.execute(insert_sql,parm)
# conn.commit()

parm_list=[('小红帽',8),('红太狼',12),('懒洋洋',5),('喜洋洋',7)]
# parm_list=[(8,'小红帽'),(12,'红太狼'),(5,'懒洋洋'),(7,'喜洋洋')]
insert_sql="insert into student values(%s,%s)"
# for i in range(4):
#     parm=parm_list[i]
#     print(parm)
#     cursor.execute(insert_sql,(parm[1],parm[0]))
# conn.commit()

# 简便方法(参数为嵌套序列)
# cursor.executemany(insert_sql,parm_list)
# conn.commit()


# 提取数据
select_sql="select * from student limit 4"
cursor.execute(select_sql)
# 提取一条信息
# print(cursor.fetchone())# 返回元组
# 提取多条信息
# print(cursor.fetchmany(4))# 嵌套的元组
# 提取所有信息
# print(cursor.fetchall())# 嵌套的元组


# 修改数据
update_sql="update student set age=%s where studentName=%s"
parm=(100,"红太狼")
# cursor.execute(update_sql,parm)
# # update语句练习
# parmlist=(('小红帽',100),('红太狼',200),('懒洋洋',300),('喜洋洋',400))
# conn.commit()


# # 删除数据
# delete_sql="delete from student where age>80"
# cursor.execute(delete_sql)
# conn.commit()

# # 创建一个自增列的表
# create_sql="""
# create table if not exists test(id int primary key auto_increment,studentName varchar(255) not null,
# age int not null)
# """
# cursor.execute(create_sql)
# insert_sql="insert into test values(null,%s,%s)"
# s='abcdefghij'
# for i in range(1,11):
#     cursor.execute(insert_sql,("小%s同学"%s[i-1],i*10))
# conn.commit()

# mysql练习题
# 1.查询'007'课程的最高分
# 2．查询平均成绩大于60分的同学的学号和平均成绩
# 3.查询学过“李纯”老师课的同学的学号、姓名
# 4.查询学过“002”并且也学过编号“003”课程的同学的学号、姓名
# 5．查询“002”课程比“003”课程成绩高的所有学生的学号

# 关闭游标
cursor.close()
conn.close()




