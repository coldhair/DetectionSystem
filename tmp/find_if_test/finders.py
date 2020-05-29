import re
import xlrd
import csv

idpat= re.compile(r'\s?(\d{17}[\d|X|x])\s?')  # 发票代码


execl_path = 'all_name1.xlsx'
excel = xlrd.open_workbook(execl_path, encoding_override='utf-8')
all_sheet = excel.sheets()
print(all_sheet)

for each_sheet in all_sheet:
    print(each_sheet.name)

sheet2 = excel.sheet_by_name(u'all_name')

# 获取前两列的内容，并合并成二维列表
p0=sheet2.col_values(0)
p1=sheet2.col_values(1)
p=list(zip(p0,p1))

print(p)


idlist=[]
with open('testlist1.txt',encoding='GBK') as f:
    for x in f:
        id = idpat.findall(x)[0]  # ID
        idlist.append(id)

print(idlist)

# 组装与一个二维列表
if_test=[]
for n,m in p:
    if m in idlist:
        if_test.append([str(n),str(m)+'$','yes'])
    else:
        if_test.append([str(n),str(m)+'$','no'])

print(if_test)

# 将结果写入csv表格
with open('myresult.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in if_test:
        writer.writerow(row)