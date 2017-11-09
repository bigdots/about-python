#!/usr/bin/python
# coding=utf-8
import os
import os.path
from PyPDF2 import PdfFileReader,PdfFileWriter
import time

time1=time.time()

############## 排除非pdf文件 #############
def isPdf(filename):
    return os.path.splitext(filename)[1] == '.pdf'

##########################合并同一个文件夹下所有PDF文件########################
def MergePDF(filedir,outName):
    output=PdfFileWriter()
    outputPages=0
    filenames=os.listdir(filedir)

    print(filenames)

    # pdf_fileName=getFileName(filepath)

    for filename in filenames:
        if not isPdf(filename):
            continue

        filepath = os.path.join(filedir, filename)
        # 读取源pdf文件
        input = PdfFileReader(open(filepath, "rb"))

        # 如果pdf文件已经加密，必须首先解密才能使用pyPdf
        # if input.isEncrypted == True:
        #     input.decrypt("map")

        # 获得源pdf文件中页面总数
        pageCount = input.getNumPages()
        outputPages += pageCount

        # 分别将page添加到输出output中
        for iPage in range(0, pageCount):
            output.addPage(input.getPage(iPage))

    print("总页数："+str(outputPages))
    outPath = os.path.join(filedir, outName)
    # 最后写pdf文件
    output.write(open(outPath, 'wb'))
    print("合并成功")


if __name__ == '__main__': #当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
    # file_dir = input('请输入文件夹地址：')
    file_dir = os.getcwd()+'/pdfs'
    outName = input('请输入打包后的文件名称：')
    MergePDF(file_dir,outName)
    time2 = time.time()
    print(u'总共耗时：' + str(time2 - time1) + 's')
