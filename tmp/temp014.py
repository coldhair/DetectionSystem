import sys

with open('E:\myPython\DetectionSystem\Meal_ordering.txt','rt',encoding='utf8') as f:
    data=f.read()
    print(data)
    for line in f:
        print('--', line)

t=sys.getdefaultencoding() # 获得系统编码
print(t)