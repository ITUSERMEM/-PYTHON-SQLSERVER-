from tkinter import ttk

import pymssql
import tkinter as tk
import tkinter.messagebox
def h_delet():
    connect = pymssql.connect(host="127.0.0.1:1483", database="shopclub", charset="utf8")
    cursor = connect.cursor()
    sql4 = "delete from Shouse where hno='%s'" % (v10.get())
    try:
        cursor.execute(sql4)
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据删除成功")
    except:
        connect.rollback()
    cursor.close()
    connect.close()
def house_delete():
    window.destroy()
    global window_function
    global v10
    window_function=tk.Tk()
    window_function.title("连锁超市管理系统")
    window_function.geometry('400x250')
    tk.Label(window_function, text="删除库存", font=("黑体", 20)).grid(row=0,column=1,pady=20)
    tk.Label(window_function,text="请输入库存编号：").grid(row = 1,column =0,padx=20)
    v10 =tk.StringVar()
    entry1=tk.Entry(window_function,show=None,textvariable=v10).grid(row = 1,column =1,pady=40)
    button = tk.Button(window_function, text="删除", command=h_delet,anchor = 's').place(relx=0.2,rely=0.7)
    button2 = tk.Button(window_function, text="返回", command=cahne_main).place(relx=0.4,rely=0.7)
    window_function.mainloop()
def h_add():
    connect = pymssql.connect(host="127.0.0.1:1483", database="shopclub", charset="utf8")
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into Shouse(hno, saddress) values('%s','%s')" % (v1.get(), v2.get())
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
def add_house():
    window.destroy()
    global window_function
    global v1, v2
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("连锁超市管理系统")
    # 窗口大小
    window_function.geometry('500x250')
    # 生成标签
    tk.Label(window_function, text="添加仓库", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    tk.Label(window_function, text="请输入仓库编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入仓库地址：").grid(row=2, column=0, padx=20, pady=20)

    # 定义变量记录输入信
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=v1).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=v2).grid(row=2, column=1)
    # 生成按钮
    button = tk.Button(window_function, text="添加", command=h_add).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=cahne_main).place(relx=0.5, rely=0.9)
    # 显示窗口
    window_function.mainloop()
def cahne_main():
    window_function.destroy()
    housepage()
def chan_main():
    from choicepage import choicepage
    window.destroy()
    choicepage()
def housepage():
    connect1 = pymssql.connect(host="127.0.0.1:1483", database="shopclub", charset="cp936")
    cursor1 = connect1.cursor()
    sql6 = "select hno,saddress from Shouse"
    try:
        cursor1.execute(sql6)
        results = cursor1.fetchall()
        print(results)
        fields = [field[0] for field in cursor1.description]
        res = [dict(zip(fields, result)) for result in results]
        print(res)
        index = len(res)
    except:
        return
    cursor1.close()
    connect1.close()
    global window
    window = tk.Tk()
    window.title("连锁超市管理系统")
    window.geometry('500x400')
    page = tk.Frame(window)
    page.pack()
    tk.Label(window, text="仓库管理", font=("黑体", 20)).pack(pady=10)
    def creat_page(self):
        columns = ( "hno", "saddress")
        columns_values = ("仓库编号", "仓库地址")
        self.tree_view = ttk.Treeview(self,show='headings', columns=columns)
        self.tree_view.column('hno', width=80, anchor='center')
        self.tree_view.column('saddress', width=80, anchor='center')
        self.tree_view.heading('hno', text='仓库编号')
        self.tree_view.heading('saddress', text='仓库地址')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        num = 0
        while num < index:
            self.tree_view.insert('', 'end', values=(
            res[num]['hno'], res[num]['saddress']))
            num = num + 1

        button = tk.Button(window, text="退出", command=chan_main).place(relx=0.9, rely=0.03)
        button = tk.Button(window, text="添加仓库", command=add_house).place(relx=0.02, rely=0.03)
        button = tk.Button(window, text="删除仓库", command=house_delete).place(relx=0.15, rely=0.03)

    creat_page(self=window)


if __name__ == '__main__':
    housepage()
