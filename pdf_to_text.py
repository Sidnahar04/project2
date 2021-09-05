import PyPDF2

reader=PyPDF2.PdfFileReader("report.pdf")
# print(reader.getDocumentInfo())
# print(reader.getPage(5).extractText())
x=""
for i in range(1,15):
    x+=reader.getPage(i).extractText()
with open("text.txt","w") as f:
    f.write(x)