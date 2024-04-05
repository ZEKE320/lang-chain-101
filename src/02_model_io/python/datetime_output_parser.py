from datetime import datetime

from langchain.output_parsers import DatetimeOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema import BaseMessage, HumanMessage
from langchain_openai.chat_models import ChatOpenAI

output_parser = DatetimeOutputParser()

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
)

prompt: PromptTemplate = PromptTemplate.from_template("{product}のリリース日を教えて")

result: BaseMessage = chat.invoke(
    [
        HumanMessage(content=prompt.format(product="iPhone8")),
        HumanMessage(content=output_parser.get_format_instructions()),
    ]
)

output: datetime = output_parser.parse(str(result.content))

print(output)
