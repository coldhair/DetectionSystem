# 整理不规则分割符的名字列表
import re

# 打开文件并将内容转化为一个字符串
with open('../Names.txt') as file:
    names = file.readlines()
    s = ''.join(names)

# 用re.split()进行分割字符串
namelist = re.split(r'[,，.。；;\s、\n]\s*', s)
print(namelist)
# 有两个字的名字被误伤了，中间的空格被分割成了单个字，再合并起来。
for i in range(len(namelist)):
    if len(namelist[i]) == 1 and len(namelist[i - 1]) == 1:
        namelist[i - 1] = namelist[i - 1] + namelist[i]
new_namelist = [name for name in namelist if len(name) > 1]  # 去掉单个字的成员
print(new_namelist)

for name in new_namelist:
    print(name)
