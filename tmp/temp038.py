# 计算当前月份的日期范围
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p14_date_range_for_current_month.html

from datetime import date, datetime, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date == None:
        # date.replace(year, month, day)：生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


a_day = timedelta(days=1)
first_day, last_day = get_month_range()

while first_day < last_day:
    print(first_day)
    first_day += a_day


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2020, 5, 1), datetime(2020, 6, 1), timedelta(hours=6)):
    print(d)
