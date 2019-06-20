# coding:utf-8

import glob
import io
import os
from multiprocessing import Pool

from aip import AipOcr
from docx import Document
from PyPDF2 import PdfFileReader, PdfFileWriter
from wand.color import Color
from wand.image import Image

# 将pdf文件转为二进制文件


def convert_pdf(filename, res=120):

    memo = {}

    def getPdfReader(filename):
        reader = memo.get(filename, None)
        if reader is None:
            reader = PdfFileReader(filename, strict=False)
            memo[filename] = reader
        return reader

    def run_convert(filename, res):
        pdfile = getPdfReader(filename)
        pages = pdfile.getNumPages()

        for page in range(pages):
            print('正在解析%d页' % (page+1))
            pageObj = pdfile.getPage(page)
            dst_pdf = PdfFileWriter()
            dst_pdf.addPage(pageObj)

            pdf_bytes = io.BytesIO()
            dst_pdf.write(pdf_bytes)
            pdf_bytes.seek(0)

            img = Image(file=pdf_bytes, resolution=res)
            img.compression_quality = 90
            img.background_color = Color("white")
            # img.save(filename = 'C:\\Users\\SXL47\\Desktop\\tupian.jpg')
            blob = img.make_blob('jpg')
            img.destroy()
            yield blob
    return run_convert(filename, res)


def baidu_ocr(image, APP_ID, API_KEY, SECRET_KEY):
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    return client.basicGeneral(image)


def acquire_word(filename, APP_ID, API_KEY, SECRET_KEY):
    for image in convert_pdf(filename):
        try:
            pool = Pool(5)
            for word in baidu_ocr(image, APP_ID, API_KEY, SECRET_KEY)['words_result']:
                yield word['words']
        except ConnectionError:
            print('发生错误，正在重新识别')
            for word in baidu_ocr(image, APP_ID, API_KEY, SECRET_KEY)['words_result']:
                yield word['words']
            

"""
    for img in convert_pdf(filename):
        print(img)
"""


def save_docs(filename, docs_name, APP_ID, API_KEY, SECRET_KEY):
    document = Document()
    print('正在写入word文件')
    try:
        for word in acquire_word(filename, APP_ID, API_KEY, SECRET_KEY):
            document.add_paragraph(word)
    except:
        print('识别中断，正在保存已识别部分')
        pass
    document.save(docs_name)
    print('保存成功')


if __name__ == "__main__":
    APP_ID = 'APP_ID'
    API_KEY = 'API_KEY'
    SECRET_KEY = 'SECRET_KEY'
    filename = r"filenmame.pdf"
    docs_name = '.\\docs_name.docx'
    save_docs(filename, docs_name, APP_ID, API_KEY, SECRET_KEY)