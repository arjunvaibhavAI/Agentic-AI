import streamlit as st
from graph import build_graph
from config import APP_TITLE

# Build the agent graph
graph = build_graph()

# Streamlit UI
st.title(APP_TITLE)
user_input = st.text_input("Your message:", placeholder="Ask about markets, stocks, or finance news...")


if st.button("Send") and user_input:
    response = graph.invoke({"messages": [("user", user_input)]})
    
    for msg in response["messages"]:
        text = None
        if hasattr(msg, "content"):
            text = msg.content
        elif isinstance(msg, tuple) and len(msg) > 1:
            text = msg[1]

        if text:
            clean_text = text.strip()

            # Skip if it's JSON, tool/system/debug output
            if (
                clean_text.startswith("{") or
                clean_text.startswith("[") or
                clean_text.lower().startswith("no news found") or
                clean_text.lower().startswith("tool call") or
                "response_time" in clean_text.lower() or
                '"query":' in clean_text.lower()
            ):
                continue

            # If it looks like raw HTML or Markdown table from tools, skip
            if (
                "<html" in clean_text.lower() or
                clean_text.startswith("|") and clean_text.endswith("|")
            ):
                continue

            # Finally display only human-readable text
            st.write(clean_text)
