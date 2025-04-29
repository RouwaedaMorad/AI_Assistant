import streamlit as st
from src.groq_server import ask_llm, initialize_groq_client, load_api_key
from groq import Groq


client = Groq(api_key=st.secrets["GROQ"]["api_key"])
api_key = load_api_key()  # Load the API key
if api_key:
    client = initialize_groq_client(api_key) 

st.title("AI Assistant")
st.write("This is a simple AI Assistant that can answer your questions.")
st.write("Ask me anything!")
# Create a text input for the user to enter their question
question = st.text_input("Enter your question here:")
# Create a button to submit the question
if st.button("Ask"):
    # Check if the question is not empty
    if question:
        # Call the ask_llm function to get the answer
        answer = ask_llm(question,client)
        # Display the answer
        st.write("Answer:", answer)
    else:
        st.write("Please enter a question.")
# Add a footer
st.write("Made with ❤️ by Rouwaeda Morad")