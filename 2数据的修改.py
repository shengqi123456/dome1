import pymysql
#1.连接数据库
da=pymysql.connect(host="127.0.0.1",user="root",password="root" ,database="demo",port=3306)
#2.创建游标
cursor=da.cursor()
# 3.执行sql语句
# sql="select database()"
# sql="select * from tags"
sql="insert into tags(tname) value (%s)"
res=cursor.execute(sql,("文学",))
# 4.获取返回结果
# print(cursor.fetchone())
print(res)
# 4.关闭连接
da.commit()
cursor.close()
da.close()