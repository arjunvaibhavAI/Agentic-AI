from state import State


def finsight_chatbot_node(state: State, llm_with_tools):
    try:
        response = llm_with_tools.invoke(state["messages"])
        return {"messages": [response]}
    except Exception as e:
        return {
            "messages": [
                ("system", f"An error occurred while processing your request: {e}")
            ]
        }
