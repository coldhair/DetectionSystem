# defaultdict的使用
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

a = sorted(d.items())
print(a)

str = '''
字符串中的字母第一次出现时，字典中没有该字母，default_factory函数调用int()为其提供一个默认值0,加法操作将计算出每个字母出现的次数。
'''
d = defaultdict(int)
for k in str:
    d[k] += 1
print('\n', d)
a = sorted(d.items())
print('\n', a)
