import re

s = '常规剂量补钙并不会导致便秘,除非服用过量的钙剂引  起高钙血症,或者孩子 本身不存在便秘,补钙后出现, 停服钙剂后好转,则需要考虑是钙剂副作用导致,但这两种情况比较少见。how are you, dear?'
# 识别中文间的英文逗号
en_comma = re.compile('[^a-zA-Z](,)[^a-zA-Z]')  # 如果‘,’的前后都不是英文字母，则认为它是中文间的英文逗号

# 英文间的空格
en_space = re.compile('[^a-zA-Z,.?](\s+)[^a-zA-Z]')

rr = re.search(en_comma, s)
print(rr)

rr = re.search(en_space, s)
print(rr)


def change_comma(matched):
    # 替换英文逗号为中文逗号
    return matched.group().replace(',', '，')


def del_space(matched):
    # 去掉中文间空格
    return ''.join(matched.group().split())


if rr:
    print(rr.group())

res = re.sub(en_comma, change_comma, s)
print(res)

res = re.sub(en_space, del_space, res)
print(res)
