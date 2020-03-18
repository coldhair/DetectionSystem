def merger(tuple):
    sta = set()
    str_lis = []
    ok = []
    for x, y in tuple:
        sta.add(x)  # 通过集合自动去重
    for m in sta:
        for n, p in tuple:
            if m == n:
                str_lis.append(p)
                str = '、'.join(str_lis)
                str = m + str
        ok.append(str)
    return '，'.join(ok)

# # 以下为测试部分
# tup = (
#     ('山东省', '吕艳朋'), ('山东省', '张立龙'), ('北京', '李小胖'), ('北京', '张云生'), ('上海', '马云琦'), ('山东省', '武先贺'), ('北京', '李强'))
# print(merger(tup))
