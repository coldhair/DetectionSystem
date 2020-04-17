import re
# 在正则表达式里面仍然可以用format()函数
s='吕艳朋'
repat=re.compile(r'{}|张飞'.format(s))
print(repat)
p=repat.findall('吕艳朋是好人')
print(p)
