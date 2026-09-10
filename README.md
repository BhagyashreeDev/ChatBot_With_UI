# LangGraph + Streamlit AI Chatbot

A step-by-step implementation of an AI chatbot using **LangGraph** (Backend) and **Streamlit** (Frontend).

## Stages Completed So Far

### 🔹 Stage 1: Basic LangGraph Agent & Streamlit UI
- Files: [langgraph_backend.py](file:///c:/Users/Lenovo/OneDrive/Desktop/AI/ChatBot_With_UI/langgraph_backend.py), [streamlit_frontend.py](file:///c:/Users/Lenovo/OneDrive/Desktop/AI/ChatBot_With_UI/streamlit_frontend.py)
- Integrated `ChatGoogleGenerativeAI` (`gemini-flash-lite-latest`) with LangGraph `StateGraph`.
- Used `InMemorySaver` for basic state management.

### 🔹 Stage 2: Streaming & Session Thread Handling
- Files: [streamlit_frontend_streaming.py](file:///c:/Users/Lenovo/OneDrive/Desktop/AI/ChatBot_With_UI/streamlit_frontend_streaming.py), [streamlit_frontend_threading.py](file:///c:/Users/Lenovo/OneDrive/Desktop/AI/ChatBot_With_UI/streamlit_frontend_threading.py)
- Added real-time token response streaming in Streamlit UI.
- Implemented multi-thread session management.

### 🔹 Stage 3: Persistent SQLite Database Checkpointing
- Files: [langgraph_database_backend.py](file:///c:/Users/Lenovo/OneDrive/Desktop/AI/ChatBot_With_UI/langgraph_database_backend.py), [streamlit_database_frontend.py](file:///c:/Users/Lenovo/OneDrive/Desktop/AI/ChatBot_With_UI/streamlit_database_frontend.py)
- Replaced in-memory saver with `SqliteSaver` (`chatbot.db`) to persist chat messages across restarts.
- Enabled sidebar thread history selection and chat retrieval from SQLite database checkpoints.

---

## Setup Instructions

1. Clone repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ChatBot_With_UI.git
   cd ChatBot_With_UI
