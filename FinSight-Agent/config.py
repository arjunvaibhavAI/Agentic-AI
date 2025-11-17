import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Model configuration
LLM_MODEL_NAME = "llama-3.1-8b-instant"

# Streamlit App Title
APP_TITLE = "FinSight Agent — AI-Powered Market Intelligence"
