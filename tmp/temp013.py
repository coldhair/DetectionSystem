# 2.12 审查清理文本字符串

import sys
import unicodedata

digitmap = {c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(digitmap)
print(len(digitmap))
x = '\u0661\u0662\u0663'
print(x)
print(x.translate(digitmap))

s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
a = s.translate(remap)
print(a)
b = unicodedata.normalize('NFD', a)
print(b)
b.encode('ascii', 'ignore').decode('ascii')
print(b)
