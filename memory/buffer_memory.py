from dotenv import load_dotenv
import os

load_dotenv()
os.getenv("OPENAI_API_KEY")

from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)

memory.save_context(
    {"input": "AIとは何？"},
    {"output": "AIとは、人工知能のことです。"},
)
print(memory.load_memory_variables({}))

from langchain.llms import OpenAI
from langchain.chains import ConversationChain

llm = OpenAI(model_name="text-davinci-003")
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)

conversation("AIとは何？")
conversation("より詳しく教えて。")