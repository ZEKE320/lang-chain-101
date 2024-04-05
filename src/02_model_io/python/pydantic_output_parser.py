from langchain.output_parsers import PydanticOutputParser
from langchain.schema import HumanMessage
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model="gpt-3.5-turbo")


class Smartphone(BaseModel):
    release_date: str = Field(description="スマートフォンの発売日")
    screen_inches: float = Field(description="スマートフォンの画面サイズ（インチ）")
    os_installed: str = Field(description="スマートフォンにインストールされているOS")
    sp_model_name: str = Field(description="スマートフォンのモデル名")

    @validator("screen_inches")
    def validate_screen_inches(cls, field):
        if field <= 0:
            raise ValueError("Screen inches must be positive number")
        return field


parser = PydanticOutputParser(pydantic_object=Smartphone)

result = chat.invoke(
    [
        HumanMessage(content="Androidでリリースしたスマートフォンを1個挙げて"),
        HumanMessage(content=parser.get_format_instructions()),
    ]
)

parsed_result = parser.parse(str(result.content))

print(f"モデル名: {parsed_result.sp_model_name}")
