from langchain.schema import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
)

result: BaseMessage = chat.invoke(
    [
        HumanMessage(content="こんにちは！"),
    ]
)

print(result)
