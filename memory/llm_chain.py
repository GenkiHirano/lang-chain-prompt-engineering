from dotenv import load_dotenv
import os

load_dotenv()
os.getenv("OPENAI_API_KEY")

from langchain.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate

template = """あなたは人間と話すチャットボットです。

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=OpenAI(model_name="text-davinci-003"),
    prompt=prompt,
    verbose=True,
    memory=memory,
)

llm_chain.predict(human_input="AIとは何？")
llm_chain.predict(human_input="より詳しく教えて。")
llm_chain.predict(human_input="")
