from django.conf import settings

from PyPDF2 import PdfReader


def count_book_pages(pdf):
    read_pdf = PdfReader(pdf)
    return len(read_pdf.pages)


