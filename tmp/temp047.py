# 4.12 不同集合上元素的迭代
from itertools import chain
a=[1,2,3,4]
b=['x','y','z']
for x in chain(a,b):
    print(x)
