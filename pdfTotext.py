import docx
doc = docx.Document('demo.docx')
# Do some work with the document...
del doc
import os
import time
os.remove('demo.docx')
time.sleep(1)
from pdf2docx import Converter
pdf_file='17351504.pdf'
word_file='demo.docx'
cv = Converter(pdf_file)
cv.convert(word_file,start=0,end=None)
cv.close()
print(pdf_file,word_file,end=None)
# doc to image
import docx2txt as  d2t
import pytesseract as tess
import docx
doc = docx.Document('demo.docx')
num_pages = len(doc.sections)
tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
def extract_image(docs_file,image_folder,get_text=False):
     text=d2t.process(docs_file,image_folder)
     if(get_text):
          return text
docs_file='C:\pdf_to_doc\demo.docx'
image_folder='C:\pdf_to_doc\image_folder'
extract_image(docs_file,image_folder)
# image to  text
file = open("textform.txt", "w")
for i in range(num_pages):
  i=i+1
  images='image_folder\image'+str(i)+'.png'
  print(images)
  img=Image.open(images)
  text= tess.image_to_string(img)
  file.write(text)

