
from tkinter import *
from tkinter import messagebox
from choicepage import choicepage
import pymssql

class zhuce(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text='用户名')
        self.label01.grid(row=0, column=0)

        v1 = StringVar()  # 用户名输入
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=0, column=1, columnspan=2)

        self.label02 = Label(self, text='密码')
        self.label02.grid(row=1, column=0)

        v2 = StringVar()  # 密码输入
        self.entry02 = Entry(self, textvariable=v2, show='*')
        self.entry02.grid(row=1, column=1, columnspan=2)

        self.label03 = Label(self, text='确认密码')
        self.label03.grid(row=2, column=0)

        v3 = StringVar()  # 确认密码输入
        self.entry03 = Entry(self, textvariable=v3, show='*')
        self.entry03.grid(row=2, column=1, columnspan=2)

        self.label04 = Label(self, text='姓名')
        self.label04.grid(row=3, column=0)

        v4 = StringVar()  # 姓名输入
        self.entry04 = Entry(self, textvariable=v4)
        self.entry04.grid(row=3, column=1, columnspan=2)

        self.label05 = Label(self, text='性别')
        self.label05.grid(row=4, column=0)

        v5 = StringVar()  # 性别输入
        self.entry05 = Entry(self, textvariable=v5)
        self.entry05.grid(row=4, column=1, columnspan=2)

        Button(self, text='确定', command=self.login1) \
            .grid(row=5, column=1, padx=10, sticky=NSEW)
        Button(self, text='取消', command=self.cancel) \
            .grid(row=5, column=2, sticky=NSEW)

    def login1(self):
        self.connect = pymssql.connect(host="127.0.0.1:1483", database="shopclub", charset="utf8")  # 服务器名，账户，密码，数据库名
        self.cursor = self.connect.cursor()
        if self.connect:
            print('连接成功')
        self.sql = "select Admins.Id,Admins.password from Admins"

        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchone()
        self.man = self.entry01.get()
        # self.pd = self.entry02.get()
        while self.result:
            print('%s|%s' % (self.result[0], self.result[1]))

            if self.result[0] == self.entry01.get() :
                self.entry01.delete(0, END)
                self.entry02.delete(0, END)
                self.entry03.delete(0, END)
                self.entry04.delete(0, END)
                self.entry05.delete(0, END)
                messagebox.showinfo(title='提示', message='用户名已注册\n请重新输入?')
                break

            else:
                self.result = self.cursor.fetchone()
        if self.entry02.get() != self.entry03.get():
            self.entry01.delete(0, END)
            self.entry02.delete(0, END)
            self.entry03.delete(0, END)
            self.entry04.delete(0, END)
            self.entry05.delete(0, END)
            messagebox.showinfo(title='提示', message='两次密码输入不同\n请重新输入?')

        else:
            self.sql1="insert into Admins(Id ,password,name,sex) values ('%s','%s','%s','%s')" % (self.entry01.get(),self.entry02.get(),self.entry04.get(),self.entry05.get())

            self.cursor.execute(self.sql1)
            self.connect.commit()
            messagebox.showinfo(title='提示', message='注册成功')
            # break

        self.cursor.close()
        self.connect.close()

    def cancel(self):
        root.quit()


class Applicantion(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):


        self.label01 = Label(self, text='用户名')
        self.label01.grid(row=0, column=0)

        v1 = StringVar()  # 用户名输入
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=0, column=1,columnspan=2)

        self.label02 = Label(self, text='密码')
        self.label02.grid(row=1, column=0)

        v2 = StringVar()  # 密码输入
        self.entry02 = Entry(self, textvariable=v2, show='*')
        self.entry02.grid(row=1, column=1, columnspan=2)

        # 登录 注册 按钮事件绑定
        Button(self, text='登录', command=self.login)\
            .grid(row=2, column=1, padx=10, sticky=NSEW)
        Button(self, text='注册', command=self.set)\
            .grid(row=2, column=2, sticky=NSEW)

    def login(self):  # 登录事件
            self.connect = pymssql.connect(host = "127.0.0.1:1483",database = "shopclub",charset="utf8")   # 服务器名，账户，密码，数据库名
            self.cursor = self.connect.cursor()
            if self.connect:
                print('连接成功')
            self.sql = "select Admins.Id,Admins.password from Admins"

            self.cursor.execute(self.sql)
            self.result = self.cursor.fetchone()
            self.man = self.entry01.get()
             #self.pd = self.entry02.get()
            while self.result:
                print('%s|%s' % (self.result[0], self.result[1]))

                if self.result[0] == self.entry01.get() and self.result[1] == self.entry02.get():

                    self.cursor.close()
                    self.connect.close()
                    root.destroy()
                    choicepage()

                else:

                    self.result = self.cursor.fetchone()
            else:
                # 账号或密码错误清空输入框
                self.entry01.delete(0, END)
                self.entry02.delete(0, END)
                messagebox.showinfo(title='提示', message='账号或密码输入错误\n请重新输入?')
                # break

            self.cursor.close()
            self.connect.close()
            exit()

    def set(self):  # 注册事件
        root1 = Tk()
        root1.geometry('300x150+210+310')
        root1.title('注册系统')
        table = zhuce(master=root1)
        root1.mainloop()




if __name__ == '__main__':
    root = Tk()
    root.geometry('300x100+200+300')
    root.title('连锁商店登录系统')
    app = Applicantion(master=root)
    root.mainloop()
