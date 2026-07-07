import fitz  # PyMuPDF


def extract_pages_from_pdf(pdf_path: str):

    document = fitz.open(pdf_path)

    pages = []

    for page_num, page in enumerate(document):

        pages.append({
            "page": page_num + 1,
            "text": page.get_text()
        })

    document.close()

    return pages