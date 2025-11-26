import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
print("Gemini API Key Loaded:", os.getenv("GEMINI_API_KEY") is not None)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_story(prompt: str) -> str:
    # use the newer model family
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    response = model.generate_content(
        f"Write a creative six-scene short comic story about: {prompt}"
    )
    return response.text

