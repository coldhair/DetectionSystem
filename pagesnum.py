from docx.oxml import ns
from docx.oxml import OxmlElement

# 下面的函数可以自动生成页码啦


def create_element(name):
    return OxmlElement(name)


def create_attribute(element, name, value):
    element.set(ns.qn(name), value)


def add_page_number(run):
    fldChar0 = create_element('w:fldChar')
    create_attribute(fldChar0, 'w:fldCharType', 'begin')

    deng = create_element('w:instrText')
    create_attribute(deng, 'xml:space', 'preserve')
    deng.text = r"="

    fldChar1 = create_element('w:fldChar')
    create_attribute(fldChar1, 'w:fldCharType', 'begin')

    instrText = create_element('w:instrText')
    create_attribute(instrText, 'xml:space', 'preserve')
    instrText.text = r"PAGE"



    fldChar2 = create_element('w:fldChar')
    create_attribute(fldChar2, 'w:fldCharType', 'end')

    numb = create_element('w:instrText')
    create_attribute(numb, 'xml:space', 'preserve')
    numb.text = r"-1"

    fldChar3 = create_element('w:fldChar')
    create_attribute(fldChar3, 'w:fldCharType', 'end')

    run._r.append(fldChar0)
    run._r.append(deng)

    run._r.append(fldChar1)
    run._r.append(instrText)

    run._r.append(fldChar2)
    run._r.append(numb)
    run._r.append(fldChar3)


# 简直像完成了一部巨著

def add_numpages(run):
    '''
    添加总页码
    :param run:
    :return:
    '''
    fldChar0 = create_element('w:fldChar')
    create_attribute(fldChar0, 'w:fldCharType', 'begin')

    deng = create_element('w:instrText')
    create_attribute(deng, 'xml:space', 'preserve')
    deng.text = r"="

    fldChar1 = create_element('w:fldChar')
    create_attribute(fldChar1, 'w:fldCharType', 'begin')

    instrText = create_element('w:instrText')
    create_attribute(instrText, 'xml:space', 'preserve')
    instrText.text = r"NUMPAGES"



    fldChar2 = create_element('w:fldChar')
    create_attribute(fldChar2, 'w:fldCharType', 'end')

    numb = create_element('w:instrText')
    create_attribute(numb, 'xml:space', 'preserve')
    numb.text = r"-2"

    fldChar3 = create_element('w:fldChar')
    create_attribute(fldChar3, 'w:fldCharType', 'end')

    run._r.append(fldChar0)
    run._r.append(deng)

    run._r.append(fldChar1)
    run._r.append(instrText)

    run._r.append(fldChar2)
    run._r.append(numb)
    run._r.append(fldChar3)


# 要把上面的函数封闭成类使用
