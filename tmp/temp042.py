# itertools.dropwhile()
# with open('passwd') as f:
#     for line in f:
#         print(line,end='')

from itertools import dropwhile
from itertools import islice

with open('passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')  # 为什么最后结果还会出现##呢？，因为只跳过开始部分的。

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

print('-' * 20)

# 下面其实是dropwhile()的原理的解释
with open('passwd') as f:
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break  # 通过这种方式把开头给跳过了！

    while line:
        print(line, end='')
        line = next(f, None)
