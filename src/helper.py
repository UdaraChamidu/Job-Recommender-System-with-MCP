# some utility tools are here

import fitz 
import os
from dotenv import load_dotenv

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from a PDF file.

    Args:
        uploaded_file (file-like object): The uploaded PDF file.
    """
    
    text = ""
    
    try:
        with fitz.open(uploaded_file) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error uploading {uploaded_file.name}: {e}")
    return text


