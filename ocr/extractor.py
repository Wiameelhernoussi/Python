import pytesseract
import fitz  # PyMuPDF

def extract_text_from_image(image_path):
    return pytesseract.image_to_string(image_path)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
