import pdfplumber

def extract_text(pdf_path):
    """Extracts text from each page of a PDF and returns a list of strings."""
    texts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            texts.append(page.extract_text() or "")
    return texts