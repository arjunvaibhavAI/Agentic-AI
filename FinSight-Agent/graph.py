from functools import partial
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

from state import State
from llm import init_llm
from tools import init_tools
from nodes import finsight_chatbot_node

def build_graph():
    llm = init_llm()
    tools = init_tools()
    llm_with_tools = llm.bind_tools(tools)

    graph = StateGraph(State)
    graph.add_node("FinSightChatBot", partial(finsight_chatbot_node, llm_with_tools=llm_with_tools))
    graph.add_node("tools", ToolNode(tools)) 

    graph.add_edge(START, "FinSightChatBot")
    graph.add_conditional_edges("FinSightChatBot", tools_condition)
    graph.add_edge("tools", "FinSightChatBot")

    return graph.compile()
