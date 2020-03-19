import re
import pymysql

db = pymysql.connect('localhost', 'root', '6579178', 'report_sys')
cursor = db.cursor()
sql ="INSERT INTO gb_info(gb_num,gb_name) VALUES (%s, %s)"

pattern=re.compile(r'^G.*\d{4}')
pattern2=re.compile(r'[\u4e00-\u9fa5].*') # 匹配中文字符
with open('gb.txt',encoding='utf8') as file:
    lines=file.readlines()
    print(lines)
    for line in lines:
        # print(line)
        sp=line.split('工作')
        # sp=[sp[0].strip(),'工作'+ sp[1].strip()]
        result=pattern.findall(line.strip())
        print('这是',result)
        result2=pattern2.findall(line.strip())

        print(result2)
        result.append(result2[0])
        print(result)
        # print(sp)
        cursor.execute(sql,result)
db.commit()