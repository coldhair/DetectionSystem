import re

string = '''
预防孩子近视，什么光源最合适?
答：自然光（阳光）
   就近视而言,近十年来,很多研究发现户外活动能够预防近视发展。但其中最重要的因素是户外,而不是活动。
   
目前具体机理还不清楚,(研究者)认为除了户外开阔、看得远以外,暴露更多自然光也可能是一个因素How is the factor, very cool. Do it。因   此每天尽量在室外活动2小时可能对孩子视力保护有好处。


在有火和电之前, 自然光几乎是人类唯一的光源,人类的眼睛也是在自然光下演化形成的,所以也可以合理推测自然光是最适合人类眼睛的光源。

'''


def clean_space(text):
    """"
    处理多余的空格
    还是存在一些问题，会把英文标点后的空格也去掉

    """
    match_regex = re.compile(u'[\u4e00-\u9fa5。\.,，：《》、\(\)（）]{1} +(?<![a-zA-Z])|\d+ +| +\d+|[a-z A-Z]+')
    should_replace_list = match_regex.findall(text)
    order_replace_list = sorted(should_replace_list, key=lambda i: len(i), reverse=True)
    for i in order_replace_list:
        if i == u' ':
            continue
        new_i = i.strip()
        text = text.replace(i, new_i)
    return text


st = ''
for line in string.splitlines():
    if line.split():  # 通过该判断去掉空行
        line = line.strip()  # 去掉段前后空格
        line = clean_space(line)  # 去掉段中多余的空格
        line = line.replace(',', '，')  # 替换英文逗号
        line = line.replace('?', '？')  # 替换英文问号
        line = line.replace('(', '（')  # 替换英文左括号
        line = line.replace(')', '）')  # 替换英文右括号
        line = line + '\n'
        st += line

print(st)
