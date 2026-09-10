import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
# with st.chat_message('user'):
#     st.text("Hi")

# with st.chat_message('assistant'):
#     st.text("How can I help you?")

# with st.chat_message('user'):
#     st.text("My name is nitish")

# user_input = st.chat_input("Type here")

# if user_input:
#     with st.chat_message('user'):
#         st.text(user_input)

CONFIG = {"configurable": {"thread_id": "thread-1"}}

# st.session_state -> dict
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

# loading the conversation history
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input('Type here')

if user_input:

    # first add the msg into msg history
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot.invoke({"messages": [HumanMessage(content=user_input)]}, config=CONFIG)

    ai_message = response["messages"][-1].content

    # Extract only text
    if isinstance(ai_message, list):
        ai_message = "".join(
            block["text"]
            for block in ai_message
            if isinstance(block, dict) and block.get("type") == "text"
        )
    else:
        ai_message = ai_message
    
    st.session_state["message_history"].append({"role": "assistant", "content": ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)