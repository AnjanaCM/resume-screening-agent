import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a single PDF file.
    """
    text = ""

    try:
        reader = PdfReader(pdf_path)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")

    return text


def extract_all_resumes(folder_path):
    """
    Read all PDF resumes from a folder.
    Returns a dictionary:
    {
        "resume1.pdf": "text...",
        "resume2.pdf": "text..."
    }
    """

    resumes = {}

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            full_path = os.path.join(folder_path, file)

            resumes[file] = extract_text_from_pdf(full_path)

    return resumes


if __name__ == "__main__":

    folder = "resumes"

    all_resumes = extract_all_resumes(folder)

    for name, text in all_resumes.items():

        print("=" * 60)
        print("Resume:", name)
        print("=" * 60)

        print(text[:1000])      # Print first 1000 characters

        print("\n")