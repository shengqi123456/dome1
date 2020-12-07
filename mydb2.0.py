import pymysql
class MyDb():
     """初始化 AttributeError"""
     def __init__(self,host,uname,pwd,bdname,port=3306):
         self.db=pymysql.connect(host,uname,pwd,bdname,port)
         self.cursor=self.db.cursor()
     def query(self,sql):
         """查询  """
         self.cursor.execute(sql)
         return self.cursor.fetchall()
     def change(self,sql,msg:tuple):
         """增 删 改 """
         res=self.cursor.execute(sql,msg)
         self.db.commit()
         return res
     def delete(self,sql,msg:tuple):
         name="小王"
         sql=f"delect from user where name={name}"
         res=self.cursor.execute(sql,msg)
         self.db.commit()
         return res
     def __del__(self):
         self.cursor.close()
         self.db.close()
if __name__ == '__main__':
    db=MyDb("127.0.0.1","root","root","demo")
    db.delete()
    # name="小王"
    # sql = f"select * from user where name='{name}'"
    # res=db.query(sql)
    # if res==():
    #     print(f"没有{name}")
    # else:
    #     print(res)
    # sql="insert into user(name,phone) value (%s,%s)"
    # res=db.change(sql,("李强","1098"))
    # print(res)

