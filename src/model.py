import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_KEY = os.getenv("MODEL_KEY")
MODEL_URL = os.getenv("MODEL_URL")
llm = ChatOpenAI(
    model=MODEL_NAME,
    api_key=MODEL_KEY,
    base_url=MODEL_URL
)
