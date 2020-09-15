""" import PyPDF2
import tkinter
import ghostscript
pdfFileObj = open('s3_test_2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(1) 
print(pageObj.extractText()) """

import camelot
tables = camelot.read_pdf('form16_prasanth.pdf', pages='1,2,3')
print('hello')
print(tables.n)

#print(tables[1].df)
print('hai')
#tables.export('itr_test_1.csv', f='excel')
#tables[3].to_excel('itr_test_6.xlsx')
tables[1].to_csv('itr_test_2.csv')
print('hello')