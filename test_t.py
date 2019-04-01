import  pymysql

con = pymysql.connect('10.10.9.235', 'root', '123456', 'nhgs')
cursor = con.cursor()
for i in range(1,70):
    sql = "insert into student_info(sid,pwd) values('T13%02d','1234')" %(i)
    print(sql)
    cursor.execute(sql)
    con.commit()
cursor.close()