# 2.13 字符串对齐
text = 'Hello World'
t = format(text, '>20')
print(t)
t = format(text, '<20')
print(t)
t = format(text, '^20')
print(t)
t = format(text, '=>20')
print(t)
t = format(text, '*^20s')
print(t)
# 同时格式化多个字符
t = '{:>20s} {:>20s}'.format('Hello', 'World')
print(t)
# 格式化数字
x = 1.2345
d = format(x, '>10')
print(d)
d = format(x, '^10.2f')
print(d)
