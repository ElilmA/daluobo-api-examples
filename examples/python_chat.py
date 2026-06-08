import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.environ["DALUOBO_API_KEY"],
    base_url=os.getenv("DALUOBO_BASE_URL", "https://api.daluobo.cc.cd/v1"),
)

response = client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {"role": "user", "content": "用一句话介绍大萝卜 API"},
    ],
)

print(response.choices[0].message.content)

