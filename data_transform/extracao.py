from PyPDF2 import PdfReader

with open("../web_scraping/anexo_1_rol.pdf", 'rb') as pdf_file:
    pdf_reader = PdfReader(pdf_file)

    num_pages = len(pdf_reader.pages)

    for pagina in range(2, num_pages):
        page = pdf_reader.pages[pagina]

        pdf_path = "../web_scraping/anexo_1_rol.pdf"
        text = page.extract_text()
        print(text)







