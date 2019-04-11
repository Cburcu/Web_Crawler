# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('pdf_name', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

page_number = pdfReader.numPages

# creating a page object
pageObj = pdfReader.getPage(0)

texts = pageObj.extractText()

# extracting text from page
#print(pageObj.extractText())

# read text
print(texts)

# closing the pdf file object
pdfFileObj.close()
