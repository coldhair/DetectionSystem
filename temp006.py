from collections import OrderedDict

od = OrderedDict()
od['foo'] = 1
od['bar'] = 2
od['spam'] = 7
od['grok'] = 4
for key in od:
    print(key, od[key])
