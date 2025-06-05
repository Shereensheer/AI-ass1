# 1. UV
# UV is a Python library designed for building and running asynchronous applications. 
# It provides a simple and efficient way to handle asynchronous tasks.

# uv_example.py
import uv

async def main():
    print("Hello from UV!")

if __name__ == "__main__":
    uv.run(main())


# 2. OpenRouter
# OpenRouter is a unified API that gives you access to hundreds of AI models through a single endpoint,
#  while automatically handling fallbacks and selecting the most cost-effective options.

# openrouter_example.py
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

completion = client.chat.completions.create(
    model="deepseek/deepseek-chat-v3-0324:free",
    messages=[
        {"role": "user", "content": "Create beautiful ASCII art."}
    ]
)

print(completion.choices[0].message.content)


# 3. LiteLLM
# LiteLLM is a Python SDK and Proxy Server (LLM Gateway) that allows you to call 100+ LLM APIs in the OpenAI format.
#  It simplifies the integration of multiple LLMs into your applications.

# litellm_example.py


from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["COHERE_API_KEY"] = "your-cohere-key"

messages = [{"content": "Hello, how are you?", "role": "user"}]

# OpenAI call
response = completion(model="gpt-3.5-turbo", messages=messages)
print(response)

# Cohere call
response = completion(model="command-nightly", messages=messages)
print(response)


