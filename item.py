import xlrd,re
sheet_ob=xlrd.open_workbook('item.xlsx',encoding_override='utf8')
sheet=sheet_ob.sheet_by_index(0)
nrows=sheet.nrows
lists=[sheet.row_values(i+1,1,5) for i in range(nrows-1)]
# for x in lists:
#     x[0]=re.sub('[(（].*[）)]','',x[0])
#     print(x)
# lists=[re.sub('[(（].*[）)]','',lists[i][0])  for i in range(nrows-1)]
# print(lists)

for i in range(nrows-1):
    lists[i][0]=re.sub('[(（].*[）)]','',lists[i][0])
    if lists[i][1]==lists[i][2]==lists[i][3]:
        print(lists[i],i)

print(lists)