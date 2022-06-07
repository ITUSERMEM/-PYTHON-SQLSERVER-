import pymssql

connect = pymssql.connect(host = "127.0.0.1:1483",database = "shopclub",charset="utf8")  # 建立连接
if connect:
    print("连接成功!")

cursor = connect.cursor()   # 创建一个游标对象,python里的sql语句都要通过cursor来执行
cursor.execute("create table Shop(shno  varchar(20) primary key,shname varchar(20) not null,shaddress varchar(30) not null)")
cursor.execute("create table Good(gno varchar(20) primary key,gname varchar(20) not null,salprice int not null,inprice int not null)")
cursor.execute("create table Staff(stno varchar(20) primary key,stname char(20) not null,sex char(10)  not null,wage int not null,pnum varchar(11) not null,shno varchar(20),wtime varchar(20),wsalary int,foreign key(shno) references shop(shno))")
cursor.execute("create table Shouse(hno varchar(20) primary key,saddress varchar(30) not null)")
cursor.execute("create table Admins(Id  varchar(20) primary key,password varchar(20) not null,name char(10) not null,sex char(10) not null) ")
cursor.execute("create table SS(Id int not null,shno  varchar(20),gno varchar(20),sdate varchar(20) not null,snumb int not null,primary key(Id,shno,gno),foreign key(shno) references Shop(shno),foreign key(gno) references Good(gno))")
cursor.execute("create table SH(gno  varchar(20),hno varchar(20),shnumb int not null,primary key(gno,hno),foreign key(gno) references Good(gno),foreign key(hno) references Shouse(hno))")
connect.commit()  #提交
cursor.close()  # 关闭游标
connect.close()  # 关闭连接
