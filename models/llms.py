from dotenv import load_dotenv
import os

load_dotenv()
os.getenv("OPENAI_API_KEY")

from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003")
llm("ITエンジニアについて30文字で教えて。")