from PyPDF2 import PdfReader, PdfWriter

# Read the pdf to be operated and create a new merged pdf
pdf_file1 = PdfReader("HELLO.pdf")
pdf_file2 = PdfReader("WORLD.pdf")
new_file = PdfWriter()

# Select the number of pages to merge pdf
new_file.add_page(pdf_file2.pages[0])
new_file.add_page(pdf_file1.pages[0])


# Export merged pdf
with open("merge.pdf", "wb") as f:
    new_file.write(f)