from tkinter import ttk

import pymssql
import tkinter as tk
import tkinter.messagebox
def s_add():
    connect = pymssql.connect(host="127.0.0.1:1483", database="shopclub", charset="utf8")
    # 创建光标
    cursor = connect.cursor()
    # 编写SQL语句
    sql = "insert into SS(shno, gno, sdate, snumb) values('%s','%s','%s','%s')" % (v1.get(), v2.get(), v3.get(),v4.get())
    # 执行SQL语句，并且输出完成提示信息，否则回滚
    try:
        cursor.execute(sql)
        connect.commit()
        tkinter.messagebox.showinfo("提示", "数据添加成功")
    except:
        connect.rollback()
        tkinter.messagebox.showinfo("提示", "库存数量无法满足订单需求")
        print("error")
    # 关闭数据库连接，防止泄露
    cursor.close()
    connect.close()
def SELECT_hist():
    window.destroy()
    connect1 = pymssql.connect(host="127.0.0.1:1483", database="shopclub", charset="cp936")
    cursor1 = connect1.cursor()
    sql = "select ID,shno, gno, sdate, snumb from SS "
    try:
        cursor1.execute(sql)
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
    global window_function
    window_function= tk.Tk()
    window_function.title("连锁超市管理系统")
    window_function.geometry('600x400')
    tk.Label(window_function, text="历史订单记录", font=("黑体", 20)).pack(pady=10)

    def creat_page(self):
        columns = ("ID", "shno", "gno", "sdate", "snumb")
        columns_values = ("ID", "商店编号", "商品编号", "交易日期", "交易数量")
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('ID', width=80, anchor='center')
        self.tree_view.column('shno', width=80, anchor='center')
        self.tree_view.column('gno', width=80, anchor='center')
        self.tree_view.column('sdate', width=80, anchor='center')
        self.tree_view.column('snumb', width=80, anchor='center')
        self.tree_view.heading('ID', text='ID')
        self.tree_view.heading('shno', text='商店编号')
        self.tree_view.heading('gno', text='商品编号')
        self.tree_view.heading('sdate', text='交易日期')
        self.tree_view.heading('snumb', text='交易数量')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        num = 0
        while num < index:
            self.tree_view.insert('', 'end', values=(
                res[num]['ID'], res[num]['shno'], res[num]['gno'], res[num]['sdate'], res[num]['snumb']))
            num = num + 1
        button9 = tk.Button(window_function, text="退出", command=cahne_main).place(relx=0.9, rely=0.03)

    creat_page(self=window_function)
def add_sell():
    window.destroy()
    global window_function
    global v1, v2, v3, v4
    # 生成窗口
    window_function = tk.Tk()
    # 窗口标题
    window_function.title("连锁超市管理系统")
    # 窗口大小
    window_function.geometry('500x400')
    # 生成标签
    tk.Label(window_function, text="销售商品", font=("黑体", 20)).grid(row=0, column=1, pady=10)
    tk.Label(window_function, text="请输入商店编号：").grid(row=1, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入商品编号：").grid(row=2, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入销售日期：").grid(row=3, column=0, padx=20, pady=20)
    tk.Label(window_function, text="请输入销售数量：").grid(row=4, column=0, padx=20, pady=20)
    # 定义变量记录输入信
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    v3 = tk.StringVar()
    v4 = tk.StringVar()
    v5 = tk.StringVar()
    # 生成输入框
    entry1 = tk.Entry(window_function, show=None, textvariable=v1).grid(row=1, column=1)
    entry2 = tk.Entry(window_function, show=None, textvariable=v2).grid(row=2, column=1)
    entry3 = tk.Entry(window_function, show=None, textvariable=v3).grid(row=3, column=1)
    entry4 = tk.Entry(window_function, show=None, textvariable=v4).grid(row=4, column=1)
    # 生成按钮
    button = tk.Button(window_function, text="添加", command=s_add).place(relx=0.3, rely=0.9)

    button2 = tk.Button(window_function, text="返回", command=cahne_main).place(relx=0.5, rely=0.9)
    # 显示窗口
    window_function.mainloop()
def cahne_main():
    window_function.destroy()
    sellpage()
def chan_main():
    from choicepage import choicepage
    window.destroy()
    choicepage()

def sellpage():
    connect1 = pymssql.connect(host="127.0.0.1:1483", database="shopclub", charset="cp936")
    cursor1 = connect1.cursor()
    sql6 = "select A1.gno,A1.hno,SUM(A2.shnumb) AS SHNUMB from SH AS A1,SH AS A2 WHERE A1.gno=A2.gno AND A1.hno=A2.hno AND A1.SHID=A2.SHID GROUP BY A1.gno,A1.hno "
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
    tk.Label(window, text="销售管理", font=("黑体", 20)).pack(pady=10)
    def creat_page(self):
        columns = ("gno",  "hno", "SHNUMB")
        columns_values = ("商品编号" "仓库编号", "库存")
        self.tree_view = ttk.Treeview(self,show='headings', columns=columns)
        self.tree_view.column('gno', width=80, anchor='center')
        self.tree_view.column('hno', width=80, anchor='center')
        self.tree_view.column('SHNUMB', width=80, anchor='center')
        self.tree_view.heading('gno', text='商品编号')
        self.tree_view.heading('hno', text='仓库编号')
        self.tree_view.heading('SHNUMB', text='库存')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        num = 0
        while num < index:
            self.tree_view.insert('', 'end', values=(
            res[num]['gno'],  res[num]['hno'], res[num]['SHNUMB']))
            num = num + 1
        button = tk.Button(window, text="退出", command=chan_main).place(relx=0.9, rely=0.03)
        button2 = tk.Button(window, text="销售商品", command=add_sell).place(relx=0.02, rely=0.03)
        button3 = tk.Button(window, text="查询历史订单", command=SELECT_hist).place(relx=0.2, rely=0.03)

    creat_page(self=window)

if __name__ == '__main__':
    sellpage()