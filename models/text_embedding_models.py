from dotenv import load_dotenv
import os

load_dotenv()
os.getenv("OPENAI_API_KEY")

from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
query_result = embeddings.embed_query("ITエンジニアについて30文字で教えて。")

print(query_result)
print(len(query_result))