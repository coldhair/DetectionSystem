with open('Names.txt') as file:
    names=file.readlines()
    s=''.join(names)
    print(s)
import re
namelist=re.split(r'[,，.。；;\s、\n]\s*',s)
print(namelist)
for i in range(len(namelist)):
    if len(namelist[i])==1 and len(namelist[i-1])==1:
        namelist[i-1]=namelist[i-1]+namelist[i]
new_namelist=[name for name in namelist if len(name)>1]
print(new_namelist)

for name in new_namelist:
    print(name)
