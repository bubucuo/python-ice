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
 
# cursor.execute("UPDATE user set password='12345678' WHERE username = '王雪梅'")



# SQL 一门编程语言，用于访问和处理数据库系统。SQL 是一种 ANSI（American National Standards Institute）标准的计算机语言，用来操作和维护关系数据库管理系统。
# SQL Search Query Language，即结构化查询语言，是一种专门用来与数据库通信的语言。


# insert 

# cursor.execute("INSERT INTO user (username, age, code, address, phone,password) VALUES ('小明', '20', '1234567890', '110', '114', '123456')")
cursor.execute("select * from user where username = '小明'")



# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print (data)

# 关闭数据库连接
db.close()