import PyPDF2

pdf_reader1 = PyPDF2.PdfFileReader(open("meetingminutes.pdf", "rb"))
pdf_reader2 = PyPDF2.PdfFileReader(open("meetingminutes2.pdf", "rb"))

pdf_writer = PyPDF2.PdfFileWriter()

for num_page in range(pdf_reader1.numPages):
    pdf_writer.addPage(pdf_reader1.getPage(num_page))
    
for num_page in range(pdf_reader2.numPages):
    pdf_writer.addPage(pdf_reader2.getPage(num_page))
    
pdf_writer.write(open("mergedmeetingminutes.pdf", "wb"))