#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import ttk
import os,shutil


# button被点击之后会被执行
def clickMe():  # 当acction被点击时,该函数则生效
    # action.configure(text=' ' + name.get())  # 设置button显示的内容
    m = numberChosen.get()
    # print(type(m))
    action.configure(state='enable')  # 将按钮设置为灰色状态，不可使用状态
    locldir = m.strip().split(':')
    os.chdir('{0}:'.format(locldir[0]))
    # print(os.listdir())
    listNO = os.listdir()
    wokrlist = []
    for i in listNO:
        # print(i[:2])
        # print(locldir[1])
        # print(locldir[1][:2])
        if i[:2] == locldir[1][:2]:
            wokrlist.append(i)
    # print(len(wokrlist))
    # print(wokrlist)
    #copy 奇数 && 偶数
    jishu = []
    oushu = []
    for p in wokrlist:
        if int(p[-1]) in [0,2,4,6,8]:
            oushu.append(p)
        else:
            jishu.append(p)
    #派发A卷
    os.chdir('I:\\试卷\A')
    testA = os.listdir()
    print(testA)
    #派发B卷
    os.chdir('I:\\试卷\B')
    testB = os.listdir()
    # print(testB)
    #开始拷贝文件
    os.chdir('{0}:'.format(locldir[0]))
    # COPY A
    for t in jishu:
        os.chdir(sourcetest+'\A')
        for g in testA:
            if os.path.isfile(g):
                os.popen(r'copy /y   I:\试卷\A\{0}  {1}'.format(g,'{0}:'.format(locldir[0])+'\\'+t))
                # print(r'copy /y   I:\试卷\A\{0}  {1}'.format(g,'{0}:'.format(locldir[0])+'\\'+t))
                print('源文件：I:\试卷\A\{0}'.format(g)+'================>>>'+locldir[0]+'\\'+t+'发送成功')
            if  os.path.isdir(g):
                os.popen(r'xcopy /e /y /i /s /c /f I:\试卷\A\{0} {1}'.format(g,'{0}:'.format(locldir[0])+'\\'+t+'\\'+g))
                print('源文件夹：I:\试卷\A\{0}'.format(g)+'==============>>>'+locldir[0]+'\\'+t+'发送成功')
    # COPY B
    for k in oushu:
        os.chdir(sourcetest+'\B')
        for j in testB:
            if os.path.isfile(j):
                os.popen(r'copy /y   I:\试卷\B\{0}  {1}'.format(j,'{0}:'.format(locldir[0])+'\\'+k))
                print('源文件：I:\试卷\B\{0}'.format(j)+'==================>>>'+locldir[0]+'\\'+k+'发送成功')
            if  os.path.isdir(j):
                os.popen(r'xcopy /e /y /i /s /c /f I:\试卷\B\{0} {1}'.format(j,'{0}:'.format(locldir[0])+'\\'+k+'\\'+j))
                print('源文件：I:\试卷\B\{0}'.format(j)+'==================>>>'+locldir[0]+'\\'+k+'发送成功')
if __name__ == '__main__':
#
        sourcetest = r'I:\试卷'
#     classno = ''
        win = tk.Tk()
        # win.geometry('150x100')
        # win.resizable('200','200')
        win.title("试题发送")  # 添加标题
        # 创建一个下拉列表
        number = tk.StringVar()
        numberChosen = ttk.Combobox(win, width=20,textvariable=number)
        numberChosen['values'] = ('E:T11', 'G:T12', 'H:T13', 'D:T20')  # 设置下拉列表的值
        numberChosen.grid(column=1, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        ttk.Label(win, text="选择班级:").grid(column=0, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行

        # 按钮
        action = ttk.Button(win, text="发送", command=clickMe)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
        action.grid(column=2, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行

        win.mainloop()  # 当调用mainloop()时,窗口才会显示出来