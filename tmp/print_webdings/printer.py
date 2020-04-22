# 这个字符数量是不全的
# http://www.alanwood.net/demos/webdings.html
import string


s=string.printable
for i in s:
    if i.isspace() == False:
        print('  <span style="font-family: Webdings; ">{}</span><span> | {} </span></br>'.format(i,i))

for i in s:
    if i.isspace() == False:
        print('  <span style="font-family: Wingdings; ">{}</span><span> | {} </span></br>'.format(i,i))

