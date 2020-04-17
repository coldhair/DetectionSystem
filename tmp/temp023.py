from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
# itemgetter函数也支持多个keys
rows_by_lname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lname)
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lame = sorted(rows, key=lambda r: (r['lname'], r['fname']))
