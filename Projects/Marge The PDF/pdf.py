from PyPDF2 import PdfMerger

AllPDF = ["Abdul-barik.pdf", "razkumary.pdf"]

OurMerger = PdfMerger()

for NewPdf in AllPDF:
    OurMerger.append(NewPdf)
    
OurMerger.write("newpdf.pdf")
OurMerger.close()