import xlrd
import time
import pymysql

execl_path = 'Tocicant.xlsx'
excel = xlrd.open_workbook(execl_path, encoding_override='utf-8')
all_sheet = excel.sheets()
print(all_sheet)

for each_sheet in all_sheet:
    print(each_sheet.name)

unit_sheet = excel.sheet_by_name(u'Unit')

# 用人单位表--unit_info 部分
unit_name = unit_sheet.cell(0, 1).value.strip()
unit_address = unit_sheet.cell(1, 1).value.strip()
unit_linkman = unit_sheet.cell(2, 1).value.strip()
unit_phone_raw = unit_sheet.cell(3, 1).value
unit_phone = str(int(unit_phone_raw))
zip_code = unit_sheet.cell(4, 1).value
Unit_info = [unit_name, unit_address, unit_linkman, unit_phone, zip_code]
print(Unit_info)

# 报告书信息表--report_info 部分
report_num = unit_sheet.cell(4, 1).value.strip()
report_date_raw = unit_sheet.cell(5, 1).value
report_date_timestamp = time.mktime(time.strptime(report_date_raw, '%Y.%m.%d'))  # 转为时间戳
report_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(report_date_timestamp))  # 转化回日期格式,mysql要求的timestamp
# print(report_date)
Report_info = [report_num, report_date]
print(Report_info)

# 仪器设备表--instrument部分
instrument = excel.sheet_by_name(u'Instruments')
print(instrument)
# table.row(rowx)
print(instrument.nrows)
nrows = instrument.nrows  # 获取表格总行数
instrument_list = [instrument.row_values(i + 1) for i in range(nrows - 1)]
print(instrument_list)

Sample_sheet=excel.sheet_by_name(u'Sampling')
s_nrows=Sample_sheet.nrows # 获取表格总行数
sample_list=[Sample_sheet.row_values(i+1) for i in range(s_nrows-1)]
print(sample_list)

