import xlrd
import time
import pymysql

execl_path = 'D:\Xray\Xray_test_data.xlsx'
excel = xlrd.open_workbook(execl_path, encoding_override='utf-8')
all_sheet = excel.sheets()
print(all_sheet)

for each_sheet in all_sheet:
    print(each_sheet.name)

sheet2 = excel.sheet_by_name(u'Employer')

# 用人单位表--unit_info 部分
unit_name = sheet2.cell(0, 1).value.strip()
unit_address = sheet2.cell(1, 1).value.strip()
unit_linkman = sheet2.cell(2, 1).value.strip()
unit_phone_raw = sheet2.cell(3, 1).value
unit_phone = str(int(unit_phone_raw))
Unit_info = [unit_name, unit_address, unit_linkman, unit_phone]

# 报告书信息表--report_info 部分
report_num = sheet2.cell(4, 1).value.strip()
report_date_raw = sheet2.cell(5, 1).value
report_date_timestamp = time.mktime(time.strptime(report_date_raw, '%Y.%m.%d'))  # 转为时间戳
report_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(report_date_timestamp))  # 转化回日期格式,mysql要求的timestamp
# print(report_date)
Report_info = [report_num, report_date]

# 仪器设备表--instrument部分
instrument_name = sheet2.cell(6, 1).value.strip()
instrument_num = str(int(sheet2.cell(7, 1).value))
print(instrument_num)
Instrument = [instrument_name, instrument_num]

# 转化回日期格式
# timestr = time.strftime('%Y-%m-%d', time.localtime(report_date_timestamp ))
# print(timestr)

Sampling = excel.sheet_by_name(u'Sampling')
sample_lists = []
for i in range(Sampling.ncols - 1):
    sample_list = Sampling.col_values(i + 1)
    station = sample_list[0].strip()
    location = sample_list[1].strip()
    product_model = sample_list[2].strip()
    service_time_raw = sample_list[3].strip()
    service_time_timestamp = time.mktime(time.strptime(service_time_raw, '%Y.%m.%d'))
    service_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(service_time_timestamp))
    test_day_raw = sample_list[4].strip()
    test_day_timestamp = time.mktime(time.strptime(test_day_raw, '%Y.%m.%d'))
    test_day = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(test_day_timestamp))
    power_light = int(sample_list[5])
    xray_light = int(sample_list[6])
    entrance = sample_list[7]
    exit_door = sample_list[8]
    left_wall = sample_list[9]
    right_wall = sample_list[10]
    top = sample_list[11]
    workbench = sample_list[12]
    exposed_num = int(sample_list[13])
    shift = sample_list[14].strip()
    sample_lists += [station, location, product_model, service_time, test_day, power_light, xray_light, entrance,
                     exit_door, left_wall, right_wall, top, workbench, exposed_num, shift],
print(sample_lists)

db = pymysql.connect('localhost', 'root', '6579178', 'report_sys')
cursor = db.cursor()

# 插入单位信息
Unit_info_sql = "INSERT INTO unit_info(unit_name, unit_address, unit_linkman, unit_phone) VALUES(%s,%s,%s,%s)"
cursor.execute(Unit_info_sql, Unit_info)  # 插入单位信息
cursor.execute("SELECT LAST_INSERT_ID()")  # 获取最后插入时的ID
unit_id_ob = cursor.fetchone()
unit_id = unit_id_ob[0]

Report_info.append(unit_id)  # 在报告书信息列表中加入unit_id

# 插入报告书信息
Report_info_sql = "INSERT INTO report_info(report_num,report_date,report_unit) VALUES(%s,%s,%s)"
cursor.execute(Report_info_sql, Report_info)  # 插入报告书信息
cursor.execute("SELECT LAST_INSERT_ID()")  # 获取往后后的ID
report_id_ob = cursor.fetchone()
report_id = report_id_ob[0]
print('这是', report_id)

for i in range(len(sample_lists)):
    sample_lists[i].append(unit_id)
    sample_lists[i].append(report_id)

print(sample_lists)

# 插入仪器设备,实际生产中不应该再这样插入了
instrument_sql = "INSERT INTO instrument(instrument_name,instrument_num) VALUES (%s,%s)"
cursor.execute(instrument_sql, Instrument)

# 插入检测样品数据信息
Xray_info_sql = "INSERT INTO xray_info(station, location, product_model, service_time, test_day, power_light, xray_light, entrance, exit_door, left_wall, right_wall, top, workbench, exposed_num, shift, unit_id, report_id) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
cursor.executemany(Xray_info_sql, sample_lists)
# cursor.execute("SELECT * FROM report_info")
db.commit()
data = cursor.fetchall()
for d in data:
    print(d)
db.close()
