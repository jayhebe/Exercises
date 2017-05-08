import PyPDF2

def add_watermark(pdf_filename, watermark_filename, output_filename):
    pdf_file_reader = PyPDF2.PdfFileReader(open(pdf_filename, "rb"))
    watermark_file_reader = PyPDF2.PdfFileReader(open(watermark_filename, "rb"))
    pdf_file_writer = PyPDF2.PdfFileWriter()
    
    watermark = watermark_file_reader.getPage(0)
    for num_page in range(pdf_file_reader.numPages):
        current_page = pdf_file_reader.getPage(num_page)
        current_page.mergePage(watermark)
        pdf_file_writer.addPage(current_page)
    
    pdf_file_writer.write(open(output_filename, "wb"))
    
add_watermark("meetingminutes.pdf", "watermark.pdf", "watermarkminutes.pdf")