from langchain_tavily import TavilySearch
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool


def init_tools():
    tavily_tool = TavilySearch(max_results=2)
    yahoo_finance_tool = YahooFinanceNewsTool()

    return [tavily_tool, yahoo_finance_tool]

