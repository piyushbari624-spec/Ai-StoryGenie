import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("Listing available models for your key:\n")
for m in genai.list_models():
    print(m.name)
