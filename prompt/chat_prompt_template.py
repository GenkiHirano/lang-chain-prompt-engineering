from dotenv import load_dotenv
import os

load_dotenv()
os.getenv("OPENAI_API_KEY")

from langchain.prompts import load_prompt

prompt = load_prompt("lc://prompts/conversation/prompt.json")
prompt_text = prompt.format(history="こんにちは、ますみです。", input="ITエンジニアについて30文字で教えて。")
print(prompt_text)