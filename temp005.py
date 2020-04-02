from _collections import defaultdict
d=defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['c'].append(4)
d['a'].append(8)
print(d)
e=defaultdict(set)
e['a'].add(1)
e['b'].add(2)
e['c'].add(4)
e['a'].add(8)
print(e)
f = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}
f['a'].add(9)
print(f)