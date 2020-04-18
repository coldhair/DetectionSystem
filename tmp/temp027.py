import json
data={
    'name':'coldhair',
    'share':100,
    'price':56.87
}
json_str=json.dumps(data)
print(json_str)
dat=json.loads(json_str)
print(dat)
# print(json_str['name'])
print(dat['name'])
with open('data.json','w') as f:
    json.dump(data,f)

with open('data.json','r') as f:
    dataf=json.load(f)

print(dataf)

d={
    'a':True,
    'b':'Hello',
    'c':None
}
print(json.dumps(d))