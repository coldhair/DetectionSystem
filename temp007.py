import pymysql

db = pymysql.connect('localhost', 'root', '6579178', 'report_sys')
curser = db.cursor()
sql = input('请输入查询语句:\n')
curser.execute(sql)
get_all = curser.fetchall()
for inf in get_all:
    print(inf)
