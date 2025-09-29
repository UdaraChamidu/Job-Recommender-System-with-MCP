# some utility tools are here

from xml.parsers.expat import model
import fitz 
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)  # create open AI client


# extract data from pdf
def extract_text_from_pdf(uploaded_file):
    """
    Extract text from a PDF file.

    Args:
        uploaded_file (file-like object): The uploaded PDF file.
    """
    
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    
    for page in doc:
        text += page.get_text()
    return text


# function for asking openai
# passing extracted data into the llm model
def ask_openai(prompt, max_tokens=150):
    """
    Ask a question to OpenAI's GPT model and get a response.

    Args:
        prompt (str): The question or prompt to send to the model.
        model (str): The model to use (default is "gpt-3.5-turbo").
        temperature (float): The temperature for response randomness (default is 0).
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content


# search for linkedin jobs
def fetch_linkedin_jobs(search_query, location="sri lanka", rows=60):
    pass


# search for nakuri jobs
def fetch_nakuri_jobs(search_query, location="sri lanka", rows=60):  # rows = maximum job units
    pass


