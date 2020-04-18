import json
from collections import OrderedDict

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data=json.loads(s,object_pairs_hook=OrderedDict)
print(data)

class JsonObject:
    def __init__(self,d):
        self.__dict__=d

data=json.loads(s,object_hook=JsonObject)
print(data.name)
print(data.shares)