import pypdf
import sys
import os

def extract_pdf(path):
    try:
        reader = pypdf.PdfReader(path)
        text = ""
        for i, page in enumerate(reader.pages):
            text += f"--- PAGE {i+1} ---\n"
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return str(e)

base_dir = r"c:\Users\48516\Downloads\Notatki na Machine Learning\ML-notatki"
pdf1 = os.path.join(base_dir, r"Prezentacje\L1 Regreska wiloraka, współiniowość, R kwadra skorygowane.pptx.pdf")
pdf2 = os.path.join(base_dir, r"Prezentacje\L2 Trendy i Sezonowość.pptx.pdf")

with open(os.path.join(base_dir, 'l1_text.txt'), 'w', encoding='utf-8') as f:
    f.write(extract_pdf(pdf1))

with open(os.path.join(base_dir, 'l2_text.txt'), 'w', encoding='utf-8') as f:
    f.write(extract_pdf(pdf2))
