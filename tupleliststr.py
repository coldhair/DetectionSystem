# 将数字、整型、浮点型的混合列表内元素全部转化为字符型，并做了部分替换
# 将二维元组转化为二维列表
def tuple_list(a):
    b = list(a)
    for i in range(len(b)):
        b[i] = list(b[i])
    return b


# 将二维列表中所有元素转为字符串型
def any_to_str(a):
    str_list = tuple_list(a)
    for i in range(len(str_list)):
        for j in range(len(str_list[i])):
            if isinstance(str_list[i][j], str):
                pass
            else:
                str_list[i][j] = str(str_list[i][j])
                if str_list[i][j] == '0.0':  # 把0.0替换成‘—’
                    str_list[i][j] = '—'
                else:
                    pass
    return str_list

# # 以下为测试部分
# b = ((1, 2, 3), (4, 5, 6,), (7, 8, 9))
# print(any_to_str(b))
