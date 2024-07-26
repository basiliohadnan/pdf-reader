import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    
    return text

def parse_fields_and_values(text):
    fields = {}
    lines = text.split('\n')
    
    for line in lines:
        if ':' in line:
            field, value = line.split(':', 1)
            fields[field.strip()] = value.strip()
    
    return fields

def main(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    fields = parse_fields_and_values(text)
    
    for field, value in fields.items():
        print(f"Field: {field}, Value: {value}")

if __name__ == "__main__":
    pdf_path = "C:\\Users\\basil\\OneDrive\\Documentos\\test\\doc.pdf"
    main(pdf_path)
