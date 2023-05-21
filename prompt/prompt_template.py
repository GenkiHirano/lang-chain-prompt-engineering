from dotenv import load_dotenv
import os

load_dotenv()
os.getenv("OPENAI_API_KEY")

from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
{subject}について30文字で教えて。
"""

prompt = PromptTemplate(
		template=template,
    input_variables=["subject"]
)
prompt_text = prompt.format(subject="ITエンジニア")
print(prompt_text)

llm = OpenAI(model_name="text-davinci-003")
print(llm(prompt_text))