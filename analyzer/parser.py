from docx import Document
import pdfplumber


def extract_text(file_path):
    if file_path.endswith(".docx"):

        doc = Document(file_path)

        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    elif file_path.endswith(".pdf"):

        text = ""

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    return "Unsupported File"