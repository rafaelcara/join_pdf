from pypdf import PdfWriter
from os.path import join

def join_pdf(files, output="./"):

    merger = PdfWriter()

    for pdf in files:
        merger.append(pdf)
    
    merger.write(join(output, "merged.pdf"))
    merger.close()
