import streamlit as st
from src.Groq_server import GroqClient

# Title
st.title("🤖 AI Assistant")

# Initialize the Groq client
client = GroqClient()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box at the bottom
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Stream assistant response
    with st.chat_message("assistant"):
        response_box = st.empty()
        full_response = ""
        for chunk in client.ask_llm(user_input):
            full_response += chunk
            response_box.markdown(full_response + "▌")  # Typing effect
        response_box.markdown(full_response)

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# ✅ Footer displayed immediately **after** chat input
st.markdown("---")
# Fixed footer with GitHub repo link
st.markdown("""
    <style>
    .fixed-footer {
        position: fixed;
        bottom: 10px;
        left: 10px;
        font-size: 14px;
        color: gray;
        z-index: 9999;
    }
    .fixed-footer a {
        color: gray;
        text-decoration: none;
    }
    .fixed-footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="fixed-footer">
        Made with ❤️ by Rouwaeda Morad · 
        <a href="https://github.com/RouwaedaMorad/AI_Assistant" target="_blank">GitHub Repo</a>
    </div>
""", unsafe_allow_html=True)
