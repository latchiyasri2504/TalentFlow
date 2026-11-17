
import re
import pdfplumber
from docx import Document


def extract_text(file_path: str) -> str:
    if file_path.lower().endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join(
                page.extract_text() or "" for page in pdf.pages
            )

    if file_path.lower().endswith(".docx"):
        document = Document(file_path)
        return "\n".join(
            paragraph.text for paragraph in document.paragraphs
        )

    raise ValueError("Only PDF and DOCX files are supported")


def extract_details(text: str) -> dict:
    email = re.search(
        r"[\w.+-]+@[\w-]+\.[\w.-]+", text
    )

    phone = re.search(
        r"\+?\d[\d\s-]{8,14}\d", text
    )

    skills_list = [
        "Python", "Java", "SQL", "FastAPI",
        "React", "HTML", "CSS", "Machine Learning"
    ]

    skills = [
        skill for skill in skills_list
        if skill.lower() in text.lower()
    ]

    return {
        "email": email.group(0) if email else None,
        "phone": phone.group(0) if phone else None,
        "skills": skills,
        "raw_text": text
    }
