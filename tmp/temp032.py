from collections import namedtuple

Subscriber = namedtuple('Subscri', ['addr', 'joined'])
sub = Subscriber('coldhair@126.com', '2020年4月20日')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))
addr, joined = sub
print(addr)
print(joined)
