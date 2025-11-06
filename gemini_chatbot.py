# gemini_chatbot.py
import os
import streamlit as st
from google import genai

# ------------------- Streamlit Page Config -------------------
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")

# ------------------- Gemini API Setup -------------------
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Please set the GEMINI_API_KEY environment variable.")
    st.stop()

client = genai.Client(api_key=api_key)

# ------------------- Chat UI -------------------
st.title("🤖 My Chatbot")
st.caption("Powered by Google Gemini")

# Sidebar - model and language selection
st.sidebar.subheader("⚙️ Settings")

model_name = st.sidebar.selectbox(
    "Choose Model",
    ["models/gemini-2.0-flash", "models/gemini-2.0-pro"]
)

# 🌍 Language Selector
selected_language = st.sidebar.selectbox(
    "Select Reply Language",
    ["Auto (Detect)", "English", "Hindi", "Spanish", "French", "German"]
)
st.session_state.selected_language = selected_language

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------- Chat Function -------------------
def chat_with_gemini(user_input):
    # Build chat history as text
    conversation = ""
    for u, a in st.session_state.chat_history:
        conversation += f"User: {u}\nAssistant: {a}\n"

    # Instruction for multilingual response
    language = st.session_state.get("selected_language", "Auto (Detect)")
    if language == "Auto (Detect)":
        instruction = "Please reply in the same language as the user's message."
    else:
        instruction = f"Please reply only in {language}."

    conversation += f"User: {user_input}\nAssistant: {instruction}\n"

    # Send to Gemini
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=conversation
        )
        reply = response.text
    except Exception as e:
        reply = f"⚠️ Error: {e}"

    return reply

# ------------------- Chat Input -------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.chat_history.append((user_input, None))

    # Get Gemini reply
    with st.spinner("Gemini is thinking..."):
        reply = chat_with_gemini(user_input)

    # Save reply
    st.session_state.chat_history[-1] = (user_input, reply)

# ------------------- Display Conversation -------------------
for user_msg, bot_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("assistant"):
        st.write(bot_msg)
