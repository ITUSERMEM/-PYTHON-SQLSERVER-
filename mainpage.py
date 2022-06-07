from tkinter import ttk

import pymssql
import tkinter as tk
import tkinter.messagebox
#数据库库存添加操作
def kadd():
    # 连接数据库
    connect = pymssql.connect(host = "127.0.0.1:1483",database = "shopclub",charset="utf8")
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql1 = "insert into SH(gno,hno,shnumb,SHTIME) values('%s','%s','%s','%s')" % (v91.get(), v92.get(),v93.get(),v94.get())
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql1)
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
        tkinter.messagebox.showinfo("提示", "商品编号不存在或仓库编号不存在")
    # 关闭数据库连接，防止泄露
    cursor.close()
    connect.close()
#数据库仓库添加操作
def hadd():
    # 连接数据库
    connect = pymssql.connect(host = "127.0.0.1:1483",database = "shopclub",charset="utf8")
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql2 = "insert into Shouse(hno,saddress) values('%s','%s')" % (v20.get(), v21.get())
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql2)
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
        print(110)
    # 关闭数据库连接，防止泄露
    cursor.close()
    connect.close()
#数据库添加操作
def gadd():
    # 连接数据库
    connect = pymssql.connect(host = "127.0.0.1:1483",database = "shopclub",charset="utf8")
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql3 = "insert into Good(gno,gname,salprice,inprice) values('%s','%s','%s','%s')" % (v1.get(), v2.get(), v3.get(), v4.get())
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql3)
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
    # 关闭数据库连接，防止泄露
    cursor.close()
    connect.close()

#数据库删除操作
def delete():
    connect = pymssql.connect(host = "127.0.0.1:1483",database = "shopclub",charset="utf8")
    cursor=connect.cursor()
    sql4 = "delete from Good where gno='%s'" % (v10.get())
    try:
        cursor.execute(sql4)
        connect.commit()
        tkinter.messagebox.showinfo("提示","数据删除成功")
    except:
        connect.rollback()
        tkinter.messagebox.showinfo("提示", "所删除的商品不存在")
    cursor.close()
    connect.close()
def update_good():
    connect = pymssql.connect(host = "127.0.0.1:1483",database = "shopclub",charset="utf8")
    cursor = connect.cursor()
    sql33="update Good set gname='%s',salprice='%s',inprice='%s'where gno='%s'"%(v55.get(),v56.get(),v57.get(),v54.get())
    try:
        cursor.execute(sql33)
        connect.commit()
        tkinter.messagebox.showinfo("提示","数据更新成功！")
    except:
        connect.rollback()
        tkinter.messagebox.showinfo("提示", "所更新的商品不存在")
    cursor.close()
    connect.close()
#查询商品信息和商品的库存信息查询
def select():
    window_function.destroy()
    global window_function2
    connect1 = pymssql.connect(host = "127.0.0.1:1483",database = "shopclub",charset="cp936")
    cursor = connect1.cursor()
    sql6 = "select Good.gno,gname,salprice,SH.hno,shnumb,saddress,SHTIME from Good join SH on Good.gno=SH.gno join Shouse on SH.hno=Shouse.hno and good.gno='%s'"%(v13.get())
    try:
        cursor.execute(sql6)
        results = cursor.fetchall()
        print(results)
        fields = [field[0] for field in cursor.description]
        res = [dict(zip(fields, result)) for result in results]
        print(res)
        index = len(res)
    except:
        return
    cursor.close()
    connect1.close()
    # 生成窗口
    window_function2 = tk.Tk()
     # 窗口标题
    window_function2.title("商品信息和商品的库存信息")
    # 窗口大小
    window_function2.geometry('900x200')
    def creat_page(self):
        columns = ("gno", "gname", "salprice", "hno", "shnumb", "saddress","SHTIME")
        columns_values = ("商品编号", "商品名", "售价", "仓库编号", "库存", "仓库地址","入库时间")
        self.tree_view = ttk.Treeview(self,show='headings', columns=columns)
        self.tree_view.column('gno', width=80, anchor='center')
        self.tree_view.column('gname', width=80, anchor='center')
        self.tree_view.column('salprice', width=80, anchor='center')
        self.tree_view.column('hno', width=80, anchor='center')
        self.tree_view.column('shnumb', width=80, anchor='center')
        self.tree_view.column('saddress', width=80, anchor='center')
        self.tree_view.column('SHTIME', width=80, anchor='center')
        self.tree_view.heading('gno', text='商品编号')
        self.tree_view.heading('gname', text='商品名')
        self.tree_view.heading('salprice', text='售价')
        self.tree_view.heading('hno', text='仓库编号')
        self.tree_view.heading('shnumb', text='库存')
        self.tree_view.heading('saddress', text='仓库地址')
        self.tree_view.heading('SHTIME', text='入库时间')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        num = 0
        while num < index:
            self.tree_view.insert('', 'end', values=(
            res[num]['gno'], res[num]['gname'], res[num]['salprice'], res[num]['hno'], res[num]['shnumb'], res[num]['saddress'], res[num]['SHTIME']))
            num = num + 1

        button = tk.Button(window_function2, text="返回", command=cahn_main).place(relx=0.5, rely=0.8)

    creat_page(self=window_function2)
def cahn_main():
    window_function2.destroy()
    Staff_select()
#添加仓库界面
def Staff_hadd():
    #构建全集变量，方便上面的函数调用
    global window_function
    global v20,v21
    #生成窗口
    window_function=tk.Tk()
    #窗口标题
    window_function.title("连锁超市管理系统")
    #窗口大小
    window_function.geometry('400x300')
    #生成标签
    tk.Label(window_function, text="添加新仓库", font=("黑体", 20)).grid(row=0,column=1,pady=10)
    tk.Label(window_function, text="请输入仓库编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入仓库地址：").grid(row=2, column=0, padx=20, pady=20)
    # 定义变量记录输入信息
    v20 = tk.StringVar()
    v21 = tk.StringVar()
    #输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=v20).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=v21).grid(row=2, column=1)
    #生成按钮
    button = tk.Button(window_function, text="添加", command=hadd).place(relx=0.3,rely=0.9)
    button2 = tk.Button(window_function, text="返回", command=chaneg_main).place(relx=0.5,rely=0.9)
    #显示窗口
    window_function.mainloop()

    # 添加库存界面
def Staff_kadd():
        # 构建全集变量，方便上面的函数调用
        global window_function
        global v91, v92, v93,v94
        # 生成窗口
        window_function = tk.Tk()
        # 窗口标题
        window_function.title("连锁超市管理系统")
        # 窗口大小
        window_function.geometry('400x500')
        # 生成标签
        tk.Label(window_function, text="添加库存", font=("黑体", 20)).grid(row=0, column=1, pady=10)
        tk.Label(window_function, text="请输入商品编号：").grid(row=1, column=0, padx=20, pady=20)
        tk.Label(window_function, text="请输入仓库编号：").grid(row=2, column=0, padx=20, pady=20)
        tk.Label(window_function, text="请输入库存量：").grid(row=3, column=0, padx=20, pady=20)
        tk.Label(window_function, text="请输入入库时间：").grid(row=4, column=0, padx=20, pady=20)
        # 定义变量记录输入信息
        v91 = tk.StringVar()
        v92 = tk.StringVar()
        v93 = tk.StringVar()
        v94 = tk.StringVar()
        # 生成输入框
        entry1 = tk.Entry(window_function, show=None, textvariable=v91).grid(row=1, column=1)
        entry2 = tk.Entry(window_function, show=None, textvariable=v92).grid(row=2, column=1)
        entry3 = tk.Entry(window_function, show=None, textvariable=v93).grid(row=3, column=1)
        entry4 = tk.Entry(window_function, show=None, textvariable=v94).grid(row=4, column=1)
        # 生成按钮
        button = tk.Button(window_function, text="添加", command=kadd).place(relx=0.3, rely=0.9)

        button2 = tk.Button(window_function, text="返回", command=chaneg_main).place(relx=0.5, rely=0.9)
        # 显示窗口
        window_function.mainloop()


#添加商品界面
def Staff_gadd():
    #构建全集变量，方便上面的函数调用
    global window_function
    global v1,v2,v3,v4
    #生成窗口
    window_function=tk.Tk()
    #窗口标题
    window_function.title("连锁超市管理系统")
    #窗口大小
    window_function.geometry('400x400')
    #生成标签
    tk.Label(window_function, text="添加新商品", font=("黑体", 20)).grid(row=0,column=1,pady=10)
    tk.Label(window_function, text="请输入商品编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function,text="请输入商品名：").grid(row = 2,column =0,padx=20,pady=20)
    tk.Label(window_function,text="请输入销售单价：").grid(row = 3,column =0,padx=20,pady=20)
    tk.Label(window_function,text="请输入商品成本：").grid(row = 4,column =0,padx=20,pady=20)
    #定义变量记录输入信息
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    v3 = tk.StringVar()
    v4 = tk.StringVar()

    #生成输入框
    entry1 = tk.Entry(window_function,show=None,textvariable=v1).grid(row = 1,column =1)
    entry2 = tk.Entry(window_function,show=None,textvariable=v2).grid(row = 2,column =1)
    entry3 = tk.Entry(window_function,show=None,textvariable=v3).grid(row = 3,column =1)
    entry4 = tk.Entry(window_function, show=None, textvariable=v4).grid(row=4, column=1)
    #生成按钮
    button = tk.Button(window_function, text="添加", command=gadd).place(relx=0.3,rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=chaneg_main).place(relx=0.5,rely=0.9)
    #显示窗口
    window_function.mainloop()

#删除商品界面
def Staff_delete():
    global window_function
    global v10
    window_function=tk.Tk()
    window_function.title("连锁超市管理系统")
    window_function.geometry('400x250')
    tk.Label(window_function, text="删除商品", font=("黑体", 20)).grid(row=0,column=1,pady=20)
    tk.Label(window_function,text="请输入商品编号：").grid(row = 1,column =0,padx=20)
    v10 =tk.StringVar()
    entry1=tk.Entry(window_function,show=None,textvariable=v10).grid(row = 1,column =1,pady=40)
    button = tk.Button(window_function, text="删除", command=delete,anchor = 's').place(relx=0.2,rely=0.7)
    button2 = tk.Button(window_function, text="返回", command=chaneg_main).place(relx=0.4,rely=0.7)
    window_function.mainloop()

def Staff_update():
    global window_function
    global v54,v55,v56,v57
    window_function=tk.Tk()
    window_function.title("连锁超市管理系统")
    window_function.geometry('500x350')
    tk.Label(window_function, text="更新商品信息", font=("黑体", 20)).grid(row=0,column=1,pady=20)
    tk.Label(window_function,text="请输入商品编号：").grid(row = 1,column =0,padx=20,pady=20)
    tk.Label(window_function,text="请输入商品名：").grid(row = 2,column =0,padx=20,pady=20)
    tk.Label(window_function, text="请输入售价：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入成本：").grid(row=4, column=0, padx=20, pady=20)
    v54=tk.StringVar()
    v55=tk.StringVar()
    v56=tk.StringVar()
    v57=tk.StringVar()
    entry1=tk.Entry(window_function,show=None,textvariable=v54).grid(row = 1,column =1)
    entry2=tk.Entry(window_function,show=None,textvariable=v55).grid(row = 2,column =1)
    entry3 = tk.Entry(window_function, show=None, textvariable=v56).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=v57).grid(row=4, column=1)
    button = tk.Button(window_function, text="更新", command=update_good).place(relx=0.2,rely=0.9)
    button2 = tk.Button(window_function, text="返回", command=chaneg_main).place(relx=0.6,rely=0.9)
    window_function.mainloop()


#条件查找商品信息和库存信息
def Staff_select():
    global window_function
    global v13
    window_function=tk.Tk()
    window_function.title("连锁超市管理系统")
    window_function.geometry('600x200')
    tk.Label(window_function, text="查找商品的商品的信息和库存信息", font=("黑体", 20)).grid(row=0,column=1,pady=20)
    tk.Label(window_function,text="请输入商品编号：").grid(row = 1,column =0,padx=20)
    v13 =tk.StringVar()
    entry1=tk.Entry(window_function,show=None,textvariable=v13).grid(row = 1,column =1,pady=20)
    button = tk.Button(window_function, text="查找", command=select).place(relx=0.3,rely=0.8)
    button2 = tk.Button(window_function, text="返回", command=chaneg_main).place(relx=0.5,rely=0.8)
    window_function.mainloop()
#添加库存界面跳转
def change_kadd():
    #销毁画布
    window.destroy()
    #生成新界面
    Staff_kadd()
#添加仓库界面跳转
def change_hadd():
    #销毁画布
    window.destroy()
    #生成新界面
    Staff_hadd()
#添加商品界面跳转
def change_gadd():
    #销毁画布
    window.destroy()
    #生成新界面
    Staff_gadd()

#删除商品界面跳转
def change_delete():
    window.destroy()
    Staff_delete()

#更新商品界面跳转
def changeg_update():
    window.destroy()
    Staff_update()


#条件查询商品界面跳转
def change_select():
    window.destroy()
    Staff_select()

#主界面跳转
def chaneg_main():
    window_function.destroy()
    mainpage()
def chan_main():
    from choicepage import choicepage
    window.destroy()
    choicepage()
#主界面
def mainpage():
    global window
    window = tk.Tk()
    window.title("连锁超市管理系统")
    window.geometry('500x450')
    #生成画布，销毁后生成新的画布实现跳转
    page = tk.Frame(window)
    page.pack()
    tk.Label(window, text="欢迎使用连锁超市信息管理系统", font=("黑体", 20)).pack(pady=10)
    button1 = tk.Button(window, text="添加商品信息", command=change_gadd).pack(pady=10)
    button2 = tk.Button(window, text="删除商品信息", command=change_delete).pack(pady=10)
    button2 = tk.Button(window, text="更新商品信息", command=changeg_update).pack(pady=10)
    button3 = tk.Button(window, text="商品入库", command=change_kadd).pack(pady=10)
    button5 = tk.Button(window, text="查找商品信息和库存信息", command=change_select).pack(pady=10)
    button6 = tk.Button(window, text="退出", command=chan_main).pack(pady=10)

    window.mainloop()

#主函数生成主界面
if __name__ == '__main__':
    mainpage()
