# FinSight Agent: Agentic AI for Finance & General Queries

FinSight Agent is an **Agentic AI assistant** that answers **finance-related** and **general knowledge** questions by intelligently selecting the right tools.  
It uses a Large Language Model (LLM) with integrated search and finance APIs for accurate, real-time insights.

## Features
- Real-time financial news from Yahoo Finance & Tavily Search.
- Multi-tool agent for both finance and general knowledge.
- Simple, interactive UI.

## Tech Stack
- **Python**, **LangChain**, **LangGraph**
- **Streamlit** (UI)
- **Groq LLM**
- **YahooFinanceNewsTool**, **TavilySearch**
- `.env`-based configuration for API keys

## Setup
```bash
git clone https://github.com/<your-username>/FinSight-Agent.git
cd FinSight-Agent
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
pip install -r requirements.txt
Create .env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
Run: streamlit run app.py
