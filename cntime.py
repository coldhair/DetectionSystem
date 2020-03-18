import time

# 输出大写中文时间
date_map = {
    0: '〇',
    1: '一',
    2: '二',
    3: '三',
    4: '四',
    5: '五',
    6: '六',
    7: '七',
    8: '八',
    9: '九'
}


def chinese2digits(num, type):
    str_num = str(num)
    result = ''
    if type == 0:
        for i in str_num:
            result = '{}{}'.format(result, date_map.get(int(i)))
    if type == 1:
        result = '{}十{}'.format(date_map.get(int(str_num[0])), date_map.get(int(str_num[1])))
    if type == 2:
        result = '十{}'.format(date_map.get(int(str_num[1])))
    if type == 3:
        result = '十'
    if type == 4:
        result = '二十'
    return result


def chinese_data(timestamp):
    t = time.localtime(timestamp)
    year = chinese2digits(t.tm_year, 0)
    date_month = t.tm_mon
    if date_month == 10:
        month = chinese2digits(date_month, 3)
    elif date_month > 10:
        month = chinese2digits(date_month, 2)
    elif date_month < 10:
        month = chinese2digits(date_month, 0)
    date_day = t.tm_mday
    if date_day < 10:
        day = chinese2digits(date_day, 0)
    elif 10 < date_day < 20:
        day = chinese2digits(date_day, 2)
    elif date_day > 20:
        day = chinese2digits(date_day, 1)
    elif date_day == 10:
        day = chinese2digits(date_day, 3)
    elif date_day == 20:
        day = chinese2digits(date_day, 4)

    return year + '年' + month + '月' + day + '日'

# 以下为测试部分
# report_date_raw = '2019.01.21'
# report_date = int(time.mktime(time.strptime(report_date_raw, '%Y.%m.%d')))
#
# print(chinese_data(report_date))
# timestamp = 155552800
# print(chinese_data(timestamp))
# print(chinese_data(time.time()))
