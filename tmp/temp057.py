import re
s='how are you, dear?'
# 英文间的逗号
en_comma=re.compile('[a-zA-Z](,)[a-zA-Z\s]')

result=en_comma.findall(s)
print(result)

rr=re.search(en_comma,s)
print(rr)
print(rr.group())

res=re.sub(en_comma,'&',s)
print(res)