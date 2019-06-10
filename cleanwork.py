import os,shutil
import glob
diskdir = r'D:\\'
mylist = os.listdir(diskdir)
# print(mylist)
work_dir  = []
for i in  mylist:
    if i[:3]   == 'T27':
        work_dir.append(i)

#deldir
deldir = []
for g in work_dir:
    deldir.append(diskdir+g)


def delfile(path):
    #   read all the files under the folder
    tlist = os.listdir(path)

    os.chdir(path)
    if len(tlist) == 0:
        print(path+'是空文件夹')
    else:
        for n in tlist:
            print(path + "文件删除开始")
            try:
                if os.path.isdir(n):
                    #   delete file
                    print(os.listdir(path))
                    shutil.rmtree(n)
                    print('文件夹删除成功！')
                if os.path.isfile(n):
                    print(os.listdir(path))
                    os.remove(path+'\{0}'.format(n))
                    print('文件删除成功！')

            except Exception as e:
                print(e)
        print(path + "文件删除完毕！！")






if __name__ == '__main__' :
        # delfile('D:\\T2501')
    for p  in deldir:
        # print(p)
        delfile(p)