
import tkinter as tk

from mainpage import mainpage
from staffpage import staffpage
from sellpage import sellpage
from housepage import housepage
def housepp():
    window1.destroy()
    housepage()
def sellpp():
    window1.destroy()
    sellpage()
def staffpp():
    window1.destroy()
    staffpage()
def mainpp():
    window1.destroy()
    mainpage()
def chan_main():
    window1.destroy()

def choicepage():
    global window1
    window1 = tk.Tk()
    window1.title("连锁超市管理系统")
    window1.geometry('600x600')
    # 生成画布，销毁后生成新的画布实现跳转
    page = tk.Frame(window1)
    page.pack()
    tk.Label(window1, text="欢迎使用连锁超市信息管理系统", font=("黑体", 20)).pack(pady=10)
    button1 = tk.Button(window1, text="商品、库存信息管理", command=mainpp,height=5,width=30).pack(pady=10)
    button2 = tk.Button(window1, text="仓库信息管理", command=housepp, height=5, width=30).pack(pady=10)
    button2 = tk.Button(window1, text="职工信息管理", command=staffpp,height=5,width=30).pack(pady=10)
    button3 = tk.Button(window1, text="销售管理", command=sellpp,height=5,width=30).pack(pady=10)
    button4 = tk.Button(window1, text="退出", command=chan_main).pack(pady=10)
    window1.mainloop()

if __name__ == '__main__':
    choicepage()