# 2.9 将Unicode文本标准化
import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1, len(s1))
print(s2, len(s2))
print(s1 == s2)  # false

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(t1)
print(ascii(t1))

t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)
print(t1 == t2)
print(t1)
print(ascii(t1))

# normalize() 第一个参数指定字符串标准化的方式。
# NFC表示字符应该是整体组成(比如可能的话就使用单一编码)，
# 而NFD表示字符应该分解为多个组合字符表示。
p = ''.join(c for c in t1 if not unicodedata.combining(c))
print(p)

s = '\ufb01'
print(s)
t = unicodedata.normalize('NFKD', s)
print(t)
print(ascii(t))
