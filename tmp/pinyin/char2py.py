from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor
from pypinyin import pinyin

with open('hanzi.txt', encoding='utf8') as f:
    str = ''.join(f.readlines()).strip()
    char_list = str.split()
    print(char_list)

doc = Document()
doc.styles['Normal'].font.name = u'Times New Roman'
doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
doc.add_paragraph()
p = doc.add_paragraph()
pp = [pinyin(wor) for wor in char_list]
a = []
for x in pp:
    y = [i[0] for i in x]
    a.append(y)

print(a)

b = [' '.join(i) for i in a]
print(b)
c = [('(' + ' ' * (len(x) + 4) + ')') for x in b]
print(c)

q = 0
runp = ''
runk = ''
while q <= 50 and b != []:
    add = b.pop(0)
    abb = c.pop(0)
    print(add)
    run = p.add_run('(' + add + ') ')
    runp += add + '    '

    q += len(add)
    if q >= 50:
        p = doc.add_paragraph()
        run = p.add_run(runp)
        p = doc.add_paragraph()
        # run = p.add_run(runk)
        q = 0
        runp = ''
        runk = ''

# print(add)

# 用hex(255)转化为十六进制控制颜色为白色



doc.save('result.docx')
