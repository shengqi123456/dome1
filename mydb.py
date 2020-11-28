import pymysql
class MyDb:
    def __init__(self):
        self.db=pymysql.connect("127.0.0.1","root","root","demo",3306)
        self.cursor=self.db.cursor()
    def query(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def change(self,sql,msg:tuple):
        res=self.cursor.execute(sql,msg)
        self.db.commit()
        return res
    def __del__(self):
        self.cursor.close()
        self.db.close()
if __name__ == '__main__':
    db=MyDb()
    sql='select * from tags'
    res=db.query(sql)
    print(res)
