import pymssql

connect = pymssql.connect(host = "127.0.0.1:1483",database = "shopclub",charset="utf8")  # 建立连接
if connect:
    print("连接成功!")
cursor = connect.cursor()
sql = "insert into Admins(Id ,password,name,sex) values ('112004010309','abc123456','华天霖','男')"
sql1 = "insert into Admins(Id ,password,name,sex) values ('112004010308','abc123456','何小东','男')"
sql2 = "insert into Admins(Id ,password,name,sex) values ('112004010312','abc123456','邰之乐','男')"
cursor.execute(sql)
cursor.execute(sql1)
cursor.execute(sql2)
connect.commit()  # 提交
cursor.close()
connect.close()

