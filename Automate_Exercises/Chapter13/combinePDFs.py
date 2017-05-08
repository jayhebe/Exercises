import os, PyPDF2

all_pdf_files = []

for each_file in os.listdir("."):
    if each_file.endswith(".pdf"):
        all_pdf_files.append(each_file)
    
all_pdf_files.sort(key=str.lower)
# print(all_pdf_files)

pdf_file_writer = PyPDF2.PdfFileWriter()
for pdf_file in all_pdf_files:
    pdf_file_obj = open(pdf_file, "rb")
    pdf_file_reader = PyPDF2.PdfFileReader(pdf_file_obj)
     
    for page_num in range(1, pdf_file_reader.numPages):
        pdf_file_writer.addPage(pdf_file_reader.getPage(page_num))
         
    # pdf_file_obj.close()
         
new_pdf_file_obj = open("allminites.pdf", "wb")
pdf_file_writer.write(new_pdf_file_obj)
new_pdf_file_obj.close()