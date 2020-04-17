import csv

with open('readpdf/some.csv') as f:
    f_csv = csv.reader(f)
    header = next(f_csv)
    print(header)
    print(len(header))
    for row in f_csv:
        print(row)

from collections import namedtuple

with open('readpdf/some.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    print(headings)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        if any(r):
            row = Row(*r)
            print(row)
            print(row.开票日期)

with open('readpdf/some.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)

# 下面这个例子非常实用

col_types = [str, str, str, str, str, str, float, int, float, int]
print(len(col_types))
with open('readpdf/some.csv') as f:
    f_csv = csv.reader(f)
    header = next(f_csv)
    for row in f_csv:
        print(zip(col_types, row))
        row = [convert(value) for convert, value in zip(col_types, row)]  # 感觉很神奇地实现了
        print(row)
