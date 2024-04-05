from pathlib import Path
from langchain.prompts import load_prompt

loaded_prompt = load_prompt(Path(Path(__file__).parent, "prompt.json"))

print(loaded_prompt.format(product="iPhone"))
