

def log(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print("当前任务已经完成.........")
    return wrapper

class MysqlConn:
    def __init__(self,host='localhost',user='root',password='123456',
                 database='class_06',charset='utf8',port=3306):
        import pymysql
        self.conn=pymysql.connect(host=host,user=user,password=password,
                database=database,charset=charset,port=port)
        self.cursor=self.conn.cursor()
        print("已经连接到数据库:%s.........."%database)


    def create_table(self,sql=None):
        if sql==None:
            sql=input("请输入创建数据库的sql语句:")
            self.cursor.execute(sql)
            self.conn.commit()
        else:
            self.cursor.execute(sql)
            self.conn.commit()

    def delete_table(self,table):
        self.cursor.execute("drop table %s" % table)
        self.conn.commit()
        print("数据表%s已经删除........" % table)

    def insert(self,info,table):
        self.cursor.execute("select * from %s"%table)
        colnames=[i[0] for i in self.cursor.description]
        self.colnames=colnames
        # print(colnames)
        insert_sql="insert into {} values({})".format(table,','.join(['%s']*len(colnames)))
        self.cursor.executemany(insert_sql,info)
        print("成功向%s表中插入%s条数据........"%(table,len(info)))
        self.conn.commit()


    def select(self,sql=None):
        import pandas as pd
        if sql==None:
            sql=input("请输入提取数据的sql语句:")
            return pd.read_sql(sql,self.conn)
        else:
            return pd.read_sql(sql,self.conn)


    def delete(self,sql=None):
        if sql == None:
            sql = input("请输入删除数据的sql语句:")
            self.cursor.execute(sql)
            self.conn.commit()
        else:
            self.cursor.execute(sql)
            self.conn.commit()


    def update(self,sql=None):
        if sql==None:
            sql=input("请输入修改数据的sql语句:")
            self.cursor.execute(sql)
            self.conn.commit()
        else:
            self.cursor.execute(sql)
            self.conn.commit()
    @log
    def close(self):
        # print("已关闭数据库连接..........")
        self.cursor.close()
        self.conn.close()



con=MysqlConn(database="class_06")
datas=[['a1',10,100],['a1',10,100]]
# con.insert(datas,"sales")
# r=con.select("sales",10)
# print(r)
# con.delete()
# con.update("update sales set sale=sale+100")
con.create_table("create table if not exists pymysql(c1 int ,c2 int)")
# con.delete_table("pymysql")
con.close()



