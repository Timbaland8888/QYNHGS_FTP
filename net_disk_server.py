#!/usr/bin/env python
# -*- encoding:utf-8 -*-
#Arthor:Timbaland
#date:20180124
import os,sys
import Tkinter
import tkMessageBox
def net_disk(host,shardir):
    cmd = r"start \\%s%s " %(host,shardir)
    print cmd
    os.popen(cmd)

    return True
if __name__ == '__main__':
     f =os.popen('whoami').read()
     host = 'FTP'
     shardir ='\\teacher'
     print shardir
     top = Tkinter.Tk()
     top.withdraw()
     tkMessageBox.showinfo(title='何老师温馨提示您', message='请各位老师找到对应教室收作业！！！')
     net_disk(host=host,shardir=shardir)


