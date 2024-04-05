from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    streaming=True,
    model="gpt-3.5-turbo",
    callbacks=[StreamingStdOutCallbackHandler()],
)

resp = chat.invoke(input=[HumanMessage(content="おいしいステーキの焼き方を教えて")])
