import sys
sys.path.append('/RouwaedaMorad/AI_Assistant')
import src
import streamlit as st
from src import ask_llm



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
        answer = ask_llm(question)
        # Display the answer
        st.write("Answer:", answer)
    else:
        st.write("Please enter a question.")
# Add a footer
st.write("Made with ❤️ by Rouwaeda Morad")