from PyPDF2 import PdfReader 
from time import sleep
from common.stupid import fun_col, off

def read_pdf(file_name:str) -> dict:
    pdf_file = PdfReader(file_name)
    page_generator = pdf_file.pages.__iter__()
    i = 0
    while True:
        i += 1
        try:
            page = page_generator.__next__()
        except StopIteration:
            break
        
        page = page.extract_text()
        if 'TRANSACTION DESCRIPTION' not in page:
            continue
        page = page.split('\n')
        print(f'\n\n{page}\n\n')
        
        exit()

    

if __name__ == "__main__":
    # read_pdf('inputs/2020-10-16-Triangle-WorldEliteMastercard.pdf')
    pass
