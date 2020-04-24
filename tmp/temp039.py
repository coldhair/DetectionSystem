# 3.15 字符串转换为日期
from datetime import datetime

text = '2020-04-24'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)
print(z)
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)


# 自定义函数要比datetime.strptime() 快7倍多
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))


x = parse_ymd(text)
print(x)
print(y)
