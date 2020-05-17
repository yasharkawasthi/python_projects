import PyPDF2
import docx
import argparse
import os

PDFfilename = 'C:/Users/Shahnawaz/Downloads/MCA_First_Year.pdf'
OutputLocation = 'docs.docx'

a=[]

#parser = argparse.ArgumentParser(description='Extract Text from Pdf into Docx...')
#parser.add_argument('pdfFileName', type=str,help='Pdf File Name or Path to the pdf file..')
#parser.add_argument("-o",'--OutputLocation', type=str,help='Output path to store converted Pdf as .docx extension ..',default="C:/Users/Administrator/Desktop/default.docx")
#args=parser.parse_args()
#PDFfilename = args.pdfFileName #filename of your PDF/directory where your PDF is stored

pdfFileObj=open(PDFfilename,'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
for i in range(0,pdfReader.numPages):
    pageobj=pdfReader.getPage(i)
    a.append(pageobj.extractText())
pdfFileObj.close()
doc = docx.Document()

for i in range(len(a)):
    doc.add_paragraph(a[i])
    doc.add_page_break()
doc.save(OutputLocation)
