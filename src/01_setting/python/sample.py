import openai
from openai.types.chat.chat_completion import ChatCompletion

response: ChatCompletion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "そばの原材料を教えて"}],
    max_tokens=100,
    temperature=1,
    n=2,
)

print(response.model_dump_json(indent=2))
