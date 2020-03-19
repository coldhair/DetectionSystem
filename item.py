import xlrd, re
import pymysql

sheet_ob = xlrd.open_workbook('item.xlsx', encoding_override='utf8')
sheet = sheet_ob.sheet_by_index(0)
nrows = sheet.nrows
lists = [sheet.row_values(i + 1, 1, 6) for i in range(nrows - 1)]
# for x in lists:
#     x[0]=re.sub('[(（].*[）)]','',x[0])
#     print(x)
# lists=[re.sub('[(（].*[）)]','',lists[i][0])  for i in range(nrows-1)]
# print(lists)

db = pymysql.connect('localhost', 'root', '6579178', 'report_sys')
cursor = db.cursor()
sql = "INSERT INTO test_item(TEST_ITEM_NAME, MAC_LIMIT, STEL_LIMIT, TWA_LIMIT, SAMPLE_NAME) VALUES (%s, %s, %s, %s, %s)"

for i in range(nrows - 1):
    lists[i][0] = re.sub('[(（].*[）)]', '', lists[i][0])
    if lists[i][1] == lists[i][2] == lists[i][3]:
        # print(lists[i], i)
        pass
    else:
        if not isinstance(lists[i][1], float):
            lists[i][1] = None
        if not isinstance(lists[i][2], float):
            lists[i][2] = None
        if not isinstance(lists[i][3], float):
            lists[i][3] = None
        inser=[lists[i][0],lists[i][1],lists[i][2],lists[i][3],lists[i][4]]
        cursor.execute(sql,inser)
        print(inser)
db.commit()


# print(type(''),isinstance('',float))
#
# print(lists)
# #
# for ne in lists:
#     print(ne)
