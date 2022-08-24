import PyPDF2

with open('TILTIT.pdf','rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(180)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('edited1.pdf','wb') as new_file:
        writer.write(new_file)
