import pymysql
#1.连接数据库
#cursorclass=pymysql.cursors.DictCursor 指定成字典类型
da=pymysql.connect(host="127.0.0.1",user="root",password="root" ,database="demo",port=3306,cursorclass=pymysql.cursors.DictCursor)
#2.创建游标
cursor=da.cursor()
# 3.执行sql语句
# sql="select database()"
sql="select * from tags"
cursor.execute(sql)
# 4.获取返回结果
# print(cursor.fetchone())
print(cursor.fetchall())
# 4.关闭连接
cursor.close()
da.close()