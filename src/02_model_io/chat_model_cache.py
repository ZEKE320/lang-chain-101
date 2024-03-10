import time

from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache
from langchain.schema import HumanMessage
from langchain_openai import ChatOpenAI

set_llm_cache(InMemoryCache())

chat = ChatOpenAI(model="gpt-3.5-turbo")

start = time.time()
result = chat.invoke([HumanMessage(content="こんにちは！")])

end = time.time()
print(result.content)
print(f"実行時間: {end - start}秒")

start = time.time()
result = chat.invoke([HumanMessage(content="こんにちは！")])

end = time.time()
print(result.content)
print(f"実行時間: {end - start}秒")
