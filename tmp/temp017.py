# 2.15 字符串中插入变量
s = '{name} has {n} messages'
p = s.format(name='Paul', n=37)
print(p)
# --使用format_map()和vars()
# vars()返回一个字典
print(type(vars()))
name = 'Coldhair'
n = 37
print(vars())
p = s.format_map(vars())
print(p)


# vars() 还有一个有意思的特性就是它也适用于对象实例。
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Lv', 35)
p = s.format_map(vars(a))
print(p)


class SafeSub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


del n
p = s.format_map(SafeSub(vars()))
print(p)
