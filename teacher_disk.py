#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Arthur:Timbaland
# Date:2018-03
import sys,time,os,shutil,re
from  CRETE_FILES import *
reload(sys)
sys.setdefaultencoding( "utf-8" )
import os,shutil,datetime
now_date = datetime.datetime.now().strftime('%H:%M')
print now_date
sharedir= 'D:\\'
os.chdir(sharedir)
# print os.listdir(sharedir)

while True:
    for f  in  os.listdir(sharedir):
        try:
            # time.sleep(1)
            if  re.findall('A01',f) == ['A01']:
                # 判断是否是目录

                for m in  os.listdir(sharedir+f):
                        if os.path.isdir((sharedir+f)+'\\%s'%(m)):
                                srcdir = (sharedir+f)+'\\%s'%(m)
                                dstdir = sharedir+'teacher\\1403\\%s' %(m)
                                print srcdir
                                print dstdir
                                # print 'xcopy %s %s /y' %(srcdir,dstdir)
                                # shutil.copytree((sharedir+f)+'\\%s'%(m),sharedir+'teacher\\%s'%(m))
                                os.popen('xcopy /y /s /c /i "%s" %s ' %(srcdir,dstdir))
                                # print k.read()
                        else:
                            srcdir = (sharedir + f) + '\\%s' % (m)
                            dstdir = sharedir + 'teacher\\1403\\'
                            print srcdir
                            print dstdir
                            os.popen('copy  "%s" %s ' % (srcdir, dstdir))
            elif re.findall('B01',f) == ['B01']:
                for m in os.listdir(sharedir + f):
                    if os.path.isdir((sharedir + f) + '\\%s' % (m)):
                        srcdir = (sharedir + f) + '\\%s' % (m)
                        dstdir = sharedir + 'teacher\\1405\\%s' %(m)
                        print srcdir
                        print dstdir
                        # print 'xcopy %s %s /y' %(srcdir,dstdir)
                        # shutil.copytree((sharedir+f)+'\\%s'%(m),sharedir+'teacher\\%s'%(m))
                        os.popen('xcopy /y /s /c /i "%s" %s ' % (srcdir, dstdir))
                        # print k.read()
                    else:
                        srcdir = (sharedir + f) + '\\%s' % (m)
                        dstdir = sharedir + 'teacher\\1405\\'
                        print srcdir
                        print dstdir
                        # print 'xcopy %s %s /y' % (srcdir, dstdir)
                        # shutil.copytree((sharedir+f)+'\\%s'%(m),sharedir+'teacher\\%s'%(m))
                        os.popen('copy  "%s" %s ' % (srcdir, dstdir))
            elif re.findall('C01', f) == ['C01']:
                for m in os.listdir(sharedir + f):
                    if os.path.isdir((sharedir + f) + '\\%s' % (m)):
                        srcdir = (sharedir + f) + '\\%s' % (m)
                        dstdir = sharedir + 'teacher\\1407\\%s' %(m)
                        print srcdir
                        print dstdir
                        # print 'xcopy %s %s /y' %(srcdir,dstdir)
                        # shutil.copytree((sharedir+f)+'\\%s'%(m),sharedir+'teacher\\%s'%(m))
                        os.popen('xcopy /y /s /c /i "%s" %s ' % (srcdir, dstdir))
                        # print k.read()
                    else:
                        srcdir = (sharedir + f) + '\\%s' % (m)
                        dstdir = sharedir + 'teacher\\1407\\'
                        print srcdir
                        print dstdir
                        # print 'xcopy %s %s /y' % (srcdir, dstdir)
                        # shutil.copytree((sharedir+f)+'\\%s'%(m),sharedir+'teacher\\%s'%(m))
                        os.popen('copy  "%s" %s ' % (srcdir, dstdir))
            elif re.findall('D01', f) == ['D01']:
                for m in os.listdir(sharedir + f):
                    if os.path.isdir((sharedir + f) + '\\%s' % (m)):
                        srcdir = (sharedir + f) + '\\%s' % (m)
                        dstdir = sharedir + 'teacher\\1404\\%s' %(m)
                        print srcdir
                        print dstdir
                        # print 'xcopy %s %s /y' %(srcdir,dstdir)
                        # shutil.copytree((sharedir+f)+'\\%s'%(m),sharedir+'teacher\\%s'%(m))
                        os.popen('xcopy /y /s /c /i "%s" %s ' % (srcdir, dstdir))
                        # print k.read()
                    else:
                        srcdir = (sharedir + f) + '\\%s' % (m)
                        dstdir = sharedir + 'teacher\\1404\\'
                        print srcdir
                        print dstdir
                        # print 'xcopy %s %s /y' % (srcdir, dstdir)
                        # shutil.copytree((sharedir+f)+'\\%s'%(m),sharedir+'teacher\\%s'%(m))
                        os.popen('copy  "%s" %s ' % (srcdir, dstdir))


            elif re.findall('E01', f) == ['E01']:
                    for m in os.listdir(sharedir + f):

                        if os.path.isdir((sharedir + f) + "\\%s" % (m)):
                            srcdir = (sharedir + f) + "\\%s" % (m)
                            dstdir = sharedir + 'teacher\\1406\\%s' %(m)
                            print srcdir
                            print dstdir
                            # print 'xcopy %s %s /y' %(srcdir,dstdir)
                            # shutil.copytree((sharedir+f)+'\\%s'%(m),sharedir+'teacher\\%s'%(m))
                            os.popen('xcopy /y /s /c /i "%s" %s ' % (srcdir, dstdir))
                            # print k.read()
                        else:

                                srcdir = (sharedir + f) + "\\%s"% (m)
                                dstdir = sharedir + 'teacher\\1406\\'
                                print srcdir
                                print dstdir
                                # print 'xcopy %s %s /y' % (srcdir, dstdir)
                                # shutil.copytree((sharedir+f)+'\\%s'%(m),sharedir+'teacher\\%s'%(m))
                                os.popen('copy  "%s" %s  ' % (srcdir, dstdir))
                                print 'copy  %s %s ' % (srcdir, dstdir)

            else:
                print "don't copy system files "


        except Exception,e:
            # print unicode(now_date+str(f),'utf-8')
            # print os.rename(f,f+now_date)
            print e
        # time.sleep(10)
    time.sleep(2)

    if datetime.datetime.now().strftime('%H:%M') in ['03:33','03:36','04:00']  :
        for f in os.listdir(sharedir):
            try:
                # time.sleep(1)
                if re.findall('A01', f) == ['A01']:
                    # 递归不询问删除目录及文件
                    os.popen('rmdir /s/q "%s"  ' % (f))
                elif re.findall('B01', f) == ['B01']:
                    # 递归不询问删除目录及文件
                    os.popen('rmdir /s/q "%s"  ' % (f))
                elif re.findall('C01', f) == ['C01']:
                    # 递归不询问删除目录及文件
                    os.popen('rmdir /s/q "%s"  ' % (f))
                elif re.findall('D01', f) == ['D01']:
                    # 递归不询问删除目录及文件
                    os.popen('rmdir /s/q "%s"  ' % (f))
                elif re.findall('E01', f) == ['E01']:
                    # 递归不询问删除目录及文件
                    os.popen('rmdir /s/q "%s"  ' % (f))
                elif re.findall('teacher', f) == ['teacher']:
                    del_dir = 'D:\\teacher'
                    os.chdir('D:\\teacher')
                    # 递归不询问删除目录及文件
                    os.popen('rmdir /s/q "%s\\1403"  ' % (del_dir))
                    os.popen('rmdir /s/q "%s\\1404"  ' % (del_dir))
                    os.popen('rmdir /s/q "%s\\1405"  ' % (del_dir))
                    os.popen('rmdir /s/q "%s\\1406"  ' % (del_dir))
                    os.popen('rmdir /s/q "%s\\1407"  ' % (del_dir))

                else:
                    print "don't delete  files "

            except Exception, e:
                # print unicode(now_date+str(f),'utf-8')
                # print os.rename(f,f+now_date)
                print e

        for f in vm_name:
            # 定义要创建的目录
            mkpath = sharedir + str(f)
            # 调用函数
            mkdir(mkpath)
            acl_dir(f)
        time.sleep(60)

    mkdir('D:\\teacher\\1403')

    mkdir('D:\\teacher\\1404')

    mkdir('D:\\teacher\\1405')

    mkdir('D:\\teacher\\1406')

    mkdir('D:\\teacher\\1407')