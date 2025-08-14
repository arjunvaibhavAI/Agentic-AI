from langchain_groq import ChatGroq
from config import LLM_MODEL_NAME, GROQ_API_KEY


def init_llm():
    return ChatGroq(
        model=LLM_MODEL_NAME,
        api_key=GROQ_API_KEY
    )
