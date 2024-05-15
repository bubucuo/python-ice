import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     port=3307,
                     user='root',
                     password='111111',
                     database='dev')
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("select * from user where username = 'admin'")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print (data)

# 关闭数据库连接
db.close()