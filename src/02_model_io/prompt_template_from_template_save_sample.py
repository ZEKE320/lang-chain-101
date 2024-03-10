from pathlib import Path

from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    template="{product}はどこの会社が開発した製品ですか?",
    input_variables=["product"],
)

prompt.save(Path(Path(__file__).parent, "prompt.json"))
