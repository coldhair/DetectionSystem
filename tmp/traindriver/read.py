import re
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams,LTTextBox
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
import os


import csv


def parse(Path):
    parser = PDFParser(Path) #parser的意思是解析器、分析程序
    document = PDFDocument(parser)
    re_list = []

    # 判断PDF是否能够解析
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBox)):
                    results = x.get_text()
                    re_list.append(results)
    print(re_list)
    return re_list




if __name__ == '__main__':

    lis = []
    for root, dirs, files in os.walk(r"testpdf"):
        for file in files:
            print(file.split('.')[-1])
            if file.split('.')[-1] == 'pdf':
                dir = os.path.join(root, file)
                Path = open(dir, 'rb')
                invoice_info = parse(Path)
                # print(invoice_info)


