# from dotenv import load_dotenv
# from pydantic import BaseModel
from google import genai
# import ollama
# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic


# AIzaSyAXdBRzrjq1h13TIfFgQDaNOV9g-6koXq4

# load_dotenv()

# llm=ChatOpenAI(model="gpt-4.1")

# llm = ChatAnthropic(model="Claude 3 Opus")
# response = llm.invoke("How to work the cpu?")
# response = ollama.chat(model="llama2", messages=[{"role": "user", "content": "How to work the CPU?"}])
# print(response)

# print(response['text'])
client = genai.Client(api_key="AIzaSyAXdBRzrjq1h13TIfFgQDaNOV9g-6koXq4")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="what is the llm?"
)
print(response)

