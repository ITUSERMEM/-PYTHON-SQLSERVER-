from tkinter import ttk

import pymssql
import tkinter as tk
import tkinter.messagebox
def s_update():
    connect = pymssql.connect(host="127.0.0.1:1483", database="shopclub", charset="utf8")
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句

    sql = "update Staff set stname='%s',sex='%s',wage='%s',pnum='%s', shno='%s',wtime='%s',wsalary='%s'where stno='%s'" % ( v12.get(), v13.get(),v14.get(), v15.get(), v16.get(),v17.get(), v18.get(),v11.get())
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql)
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据修改成功")
    except:
        connect.rollback()
        print("error")
    # 关闭数据库连接，防止泄露
    cursor.close()
    connect.close()
def add_update():
    window.destroy()
    global window_function
    global v11, v12, v13, v14, v15, v16, v17, v18
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("连锁超市管理系统")
    # 窗口大小
    window_function.geometry('400x600')
    # 生成标签
    tk.Label(window_function, text="添加职工", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    tk.Label(window_function, text="请输入职工编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入姓名：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入性别：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入工龄：").grid(row=4, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入电话号码：").grid(row=5, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入商店编号：").grid(row=6, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入聘期：").grid(row=7, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入月薪：").grid(row=8, column=0, padx=20, pady=20)
    # 定义变量记录输入信
    v11 = tk.StringVar()
    v12 = tk.StringVar()
    v13 = tk.StringVar()
    v14 = tk.StringVar()
    v15 = tk.StringVar()
    v16 = tk.StringVar()
    v17 = tk.StringVar()
    v18 = tk.StringVar()
    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=v11).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=v12).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=v13).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=v14).grid(row=4, column=1)
    entry5 = tk.Entry(window_function, show=None, textvariable=v15).grid(row=5, column=1)
    entry6 = tk.Entry(window_function, show=None, textvariable=v16).grid(row=6, column=1)
    entry7 = tk.Entry(window_function, show=None, textvariable=v17).grid(row=7, column=1)
    entry8 = tk.Entry(window_function, show=None, textvariable=v18).grid(row=8, column=1)
    # 生成按钮
    button = tk.Button(window_function, text="修改", command=s_update).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=cahne_main).place(relx=0.5, rely=0.9)
    # 显示窗口
    window_function.mainloop()
def s_delet():
    connect = pymssql.connect(host="127.0.0.1:1483", database="shopclub", charset="utf8")
    cursor = connect.cursor()
    sql4 = "delete from Staff where stno='%s'" % (v10.get())
    try:
        cursor.execute(sql4)
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据删除成功")
    except:
        connect.rollback()
    cursor.close()
    connect.close()
def Staff_delete():
    window.destroy()
    global window_function
    global v10
    window_function=tk.Tk()
    window_function.title("连锁超市管理系统")
    window_function.geometry('400x250')
    tk.Label(window_function, text="删除员工", font=("黑体", 20)).grid(row=0,column=1,pady=20)
    tk.Label(window_function,text="请输入员工编号：").grid(row = 1,column =0,padx=20)
    v10 =tk.StringVar()
    entry1=tk.Entry(window_function,show=None,textvariable=v10).grid(row = 1,column =1,pady=40)
    button = tk.Button(window_function, text="删除", command=s_delet,anchor = 's').place(relx=0.2,rely=0.7)
    button2 = tk.Button(window_function, text="返回", command=cahne_main).place(relx=0.4,rely=0.7)
    window_function.mainloop()
def s_add():
    connect = pymssql.connect(host="127.0.0.1:1483", database="shopclub", charset="utf8")
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Staff(stno, stname, sex, wage, pnum, shno,wtime,wsalary) values('%s','%s','%s','%s','%s','%s','%s','%s')" % (v1.get(), v2.get(), v3.get(),v4.get(), v5.get(), v6.get(),v7.get(), v8.get())
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql)
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
        print("error")
    # 关闭数据库连接，防止泄露
    cursor.close()
    connect.close()
def add_staf():
    window.destroy()
    global window_function
    global v1, v2, v3, v4, v5, v6, v7, v8
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("连锁超市管理系统")
    # 窗口大小
    window_function.geometry('400x600')
    # 生成标签
    tk.Label(window_function, text="添加职工", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    tk.Label(window_function, text="请输入职工编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入姓名：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入性别：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入工龄：").grid(row=4, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入电话号码：").grid(row=5, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入商店编号：").grid(row=6, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入聘期：").grid(row=7, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入月薪：").grid(row=8, column=0, padx=20, pady=20)
    # 定义变量记录输入信
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    v3 = tk.StringVar()
    v4 = tk.StringVar()
    v5 = tk.StringVar()
    v6 = tk.StringVar()
    v7 = tk.StringVar()
    v8 = tk.StringVar()
    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=v1).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=v2).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=v3).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=v4).grid(row=4, column=1)
    entry5 = tk.Entry(window_function, show=None, textvariable=v5).grid(row=5, column=1)
    entry6 = tk.Entry(window_function, show=None, textvariable=v6).grid(row=6, column=1)
    entry7 = tk.Entry(window_function, show=None, textvariable=v7).grid(row=7, column=1)
    entry8 = tk.Entry(window_function, show=None, textvariable=v8).grid(row=8, column=1)
    # 生成按钮
    button = tk.Button(window_function, text="添加", command=s_add).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=cahne_main).place(relx=0.5, rely=0.9)
    # 显示窗口
    window_function.mainloop()
def cahne_main():
    window_function.destroy()
    staffpage()
def chan_main():
    from choicepage import choicepage
    window.destroy()
    choicepage()
def staffpage():
    connect1 = pymssql.connect(host="127.0.0.1:1483", database="shopclub", charset="cp936")
    cursor1 = connect1.cursor()
    sql6 = "select stno, stname, sex, wage, pnum, shno,wtime,wsalary from Staff"
    try:
        cursor1.execute(sql6)
        results = cursor1.fetchall()
        print(results)
        fields = [field[0] for field in cursor1.description]
        res = [dict(zip(fields, result)) for result in results]
        print(res)
        index=len(res)
    except:
        return
    cursor1.close()
    connect1.close()
    global window
    window = tk.Tk()
    window.title("连锁超市管理系统")
    window.geometry('1000x600')
    # 生成画布，销毁后生成新的画布实现跳转
    page = tk.Frame(window)
    page.pack()
    tk.Label(window, text="员工管理", font=("黑体", 20)).pack(pady=10)

    def creat_pagee(self):
        columns = ("stno", "stname", "sex", "wage", "pnum", "shno","wtime","wsalary")
        columns_values = ("职工编号", "姓名", "性别", "工龄", "电话号码", "商店编号","聘期","月薪")
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('stno', width=80, anchor='center')
        self.tree_view.column('stname', width=80, anchor='center')
        self.tree_view.column('sex', width=80, anchor='center')
        self.tree_view.column('wage', width=80, anchor='center')
        self.tree_view.column('pnum', width=80, anchor='center')
        self.tree_view.column('shno', width=80, anchor='center')
        self.tree_view.column('wtime', width=80, anchor='center')
        self.tree_view.column('wsalary', width=80, anchor='center')
        self.tree_view.heading('stno', text='职工编号')
        self.tree_view.heading('stname', text='姓名')
        self.tree_view.heading('sex', text='性别')
        self.tree_view.heading('wage', text='工龄')
        self.tree_view.heading('pnum', text='电话号码')
        self.tree_view.heading('shno', text='商店编号')
        self.tree_view.heading('wtime', text='聘期')
        self.tree_view.heading('wsalary', text='月薪')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        num=0
        while num<index:
            self.tree_view.insert('', 'end', values=(
            res[num]['stno'], res[num]['stname'], res[num]['sex'], res[num]['wage'], res[num]['pnum'], res[num]['shno'],res[num]['wtime'], res[num]['wsalary']))
            num=num+1

        button = tk.Button(window, text="退出", command=chan_main).place(relx=0.9, rely=0.03)
        button = tk.Button(window, text="添加员工", command=add_staf).place(relx=0.02, rely=0.03)
        button = tk.Button(window, text="更新员工信息", command=add_update).place(relx=0.2, rely=0.03)
        button = tk.Button(window, text="删除员工", command=Staff_delete).place(relx=0.1, rely=0.03)

    creat_pagee(self=window)

if __name__ == '__main__':
    staffpage()