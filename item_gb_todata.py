import pymysql
import xlrd

# 将检测项目和对应的国家标准导入到数据库

execl = xlrd.open_workbook('item_gb.xlsx', encoding_override='utf-8')
sheet = execl.sheet_by_index(0)
print(sheet)
nrows = sheet.nrows
row_values = sheet.row_values(0)
print(row_values)
item_gb_lis = []
for i in range(nrows):
    print(sheet.row_values(i))
    row_values = sheet.row_values(i)
    for x in range(2, 5):
        if isinstance(row_values[x], float):
            item_gb = [int(row_values[0]), int(row_values[x])]
        item_gb_lis.append(item_gb)

print(item_gb_lis)
db = pymysql.connect('localhost', 'root', '6579178', 'report_sys')
curser = db.cursor()
test_item_gb_sql = "INSERT INTO test_item_gb(test_item, gb_id) VALUES (%s,%s)"
curser.executemany(test_item_gb_sql, item_gb_lis)
db.commit()
