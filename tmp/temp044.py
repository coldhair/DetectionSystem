# 4.10 序列上索引值迭代
from collections import defaultdict

my_list=['a','b','c']
for idx,val in enumerate(my_list):
    print(idx,val)

print('-'*20)
# 按传统行号输出(行号从1开始)
for idx,val in enumerate(my_list,1):
    print(idx,val)


def parse_data(filename):
    with open(filename,'rt') as f :
        for lineno,line in enumerate(f,1):
            fields=line.split()
            try:
                count=int(fields[1])

            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno,e))


word_summary = defaultdict(list)
with open('myfile','r') as f:
    lines=f.readlines()

for idx,line in enumerate(lines):
    words=[w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

