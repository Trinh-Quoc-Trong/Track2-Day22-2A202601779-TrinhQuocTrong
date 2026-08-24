import os
import sys
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("GOOGLE_API_KEY")
print(f"Key: {api_key[:5]}...")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)
try:
    res = llm.invoke([HumanMessage(content="Hello")])
    print("Chat:", res.content)
except Exception as e:
    print("Chat Error:", e)

from langchain_google_genai import GoogleGenerativeAIEmbeddings
embedder = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=api_key)
try:
    res = embedder.embed_query("Hello")
    print("Embeddings length:", len(res))
except Exception as e:
    print("Embeddings Error:", e)
