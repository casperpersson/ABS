import PyPDF2

pdf1File = open('Eksamen systemudvikling gruppe 14.pdf', 'rb')
pdf2File = open('Eksamen systemudvikling gruppe 15.pdf', 'rb')
reader1 = PyPDF2.PdfReader(pdf1File)
reader2 = PyPDF2.PdfReader(pdf2File)
writer = PyPDF2.PdfWriter()
for pageNum in range(len(reader1.pages)):
    page = reader1.pages[pageNum]
    writer.add_page(page)

for pageNum in range(len(reader2.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)

outputFile = open('CombinedPDFS.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()


