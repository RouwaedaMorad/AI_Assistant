from groq import Groq
import asyncio
import streamlit as st

from groq import Groq
import streamlit as st

class GroqClient:
    def __init__(self, api_key=None):
        if not api_key:
            api_key = st.secrets["GROQ"]["api_key"]
        self.client = Groq(api_key=api_key)

    def ask_llm(self, prompt):
        """Yields streamed LLM responses from Groq."""
        try:
            completion = self.client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[
                    {"role": "user", "content": str(prompt)}
                ],
                temperature=1,
                max_completion_tokens=1024,
                top_p=1,
                stream=True,
                stop=None,
                response_format={"format": "text"},
            )
            for chunk in completion:
                yield chunk.choices[0].delta.content or ""
        except Exception as e:
            yield f"Error: {str(e)}"


def main():
    """Main function to run the process."""
    client = GroqClient()
    full_response =""
    for chunk in client.ask_llm(prompt="Hello, how are you?"):
            full_response += chunk
    print(full_response + "▌")
   # print(client.ask_llm(prompt="Hello, how are you?"))
    
    


if __name__ == "__main__":
    main() 