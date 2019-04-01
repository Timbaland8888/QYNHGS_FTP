#!/usr/bin/env python
# -*- encoding:utf-8 -*-
#Arthor:Timbaland
#date:20180124
import os
import sys, os
# 连接mysql数据库参数字段
# con = None
# ip = '172.25.1.13'
# user = 'root'
# password = '123456'
# dbname = 'hj21_backend'
# port = 3306
# charset = 'utf8'
# db = MySQLdb.connect(host=ip, user=user, passwd=password, db=dbname, port=port, charset=charset)
# cursor = db.cursor()
# vm_name = []
# vm_room = []
#
# # 获取教室里面的虚拟机信息
# query_vm = '''SELECT wtc.terminal_name,room.classroom_name
# from wtc_terminal wtc
# INNER  JOIN wtc_classroom room on wtc.classroom_id =room.id
# '''
# try:
#     cursor.execute(query_vm)
#     result = cursor.fetchall()
#     # 获取教室云桌面数量
#     vm_count = len(result)
#     # print len(cursor.fetchall())
#     # cursor.execute(query_vm)
#     for vm_id in range(0,vm_count,1):
#         # print result[vm_id][0]
#         # print result[vm_id][1]
#         vm_name.append(result[vm_id][0])
#         vm_room.append(result[vm_id][1])
#
#     # print type(cursor.fetchall()[0])
#
#     db.commit()
#
# except ValueError:
#     db.roolback
#     print ('error')
# # 关闭游标和mysql数据库连接
# cursor.close()
# db.close()
# # print vm_name
# #crate user files

def mkdir(path):

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print (path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path + ' 目录已存在')
        return False
def acl_dir(user):
    #切换工作目录D
    os.chdir('H:\\')
    # #添加对应目录的权限
    cre_acl = 'cacls %s /e /t /g %s:F' %(user,'Everyone')
    print(cre_acl)
    os.popen(cre_acl)
    # #取消对应目录的权限
    # del_acl = 'cacls %s /e /t /c /r users' %(user)
    # os.popen(del_acl)
    #共享对应目录
    share_dir = 'net share %s=H:\\%s' %(user,user)
    print (share_dir)
    os.popen(share_dir)

if __name__ == '__main__':
    #basic dir
    bascdir = 'H:\\'

    for f in range(1,70):
        # 定义要创建的目录
        mkpath = bascdir + str('T13%02d' %(f))
        # 调用函数
        mkdir(mkpath)
        acl_dir('T13%02d' %(f))



