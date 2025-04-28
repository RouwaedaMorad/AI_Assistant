from dotenv import load_dotenv
from groq import Groq
import asyncio
import streamlit as st

# This function loads the environment variables from the .env file
def load_api_key():
    """Loads the API key from the environment."""
    load_dotenv()  # Load .env variables
    #api_key = os.getenv('GROQ_API_KEY')  # Get API key from environment
    api_key = api_key=st.secrets["openai"]["api_key"]
    if api_key:
        print("API key loaded successfully.")
    else:
        print("Failed to load API key.")
    return api_key

# This function initializes the Groq client
def initialize_groq_client(api_key):
    """Initializes the Groq client."""
    if not api_key:
        raise ValueError("API Key is required to initialize the Groq client.")
    
    client = Groq(api_key=api_key)
    return client

# This function sends a request to the Groq API and returns the completion result
def ask_llm(prompt, client):
    """Generates completions using the Groq client."""
    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": str(prompt),
                }
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
            response_format={"format": "json"},
        )
        
        # Process the streamed response using a regular loop instead of async for
        for chunk in completion:
            print(chunk.choices[0].delta.content or "", end="")
    
    except Exception as e:
        print(f"An error occurred while generating completions: {e}")

# Main function that ties everything together
async def main():
    """Main function to run the process."""
    api_key = load_api_key()  # Load the API key
    if api_key:
        client = initialize_groq_client(api_key)  # Initialize the Groq client
        
        ask_llm(client)  # Generate completions (no async needed here)

# Run the main async function
if __name__ == "__main__":
    asyncio.run(main())
