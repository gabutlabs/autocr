from google import genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
def run_agent(prompt, model="gemini-2.5-flash"):
    """Jalankan agen dengan prompt yang diberikan"""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=model, contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Error running agent: {e}")
        return None