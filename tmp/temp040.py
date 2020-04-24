from datetime import datetime
from pytz import timezone, all_timezones

# 打印所有的时区
# for tz in all_timezones:
#     print(tz)
d=datetime(2012,12,21,9,30,0)
print(d)

# localize the date for Chicago
central=timezone('US/Central')
loc_d=central.localize(d)
print(loc_d)
shanghai=timezone('Asia/Shanghai')
shanghai_d=shanghai.localize(d)
print(shanghai_d)