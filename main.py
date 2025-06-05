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


# 00_swarm/basic_swarm_simulation.py

# Simulated swarm of agents
agents = [lambda x: x + 1, lambda x: x * 2, lambda x: x - 3]

def swarm_process(input_val):
    result = input_val
    for agent in agents:
        result = agent(result)
    return result

print("Swarm Output:", swarm_process(5))  # Output: 9


# 02_openrouter/query_openrouter.py

import requests

API_KEY = "your_openrouter_api_key"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "openrouter/openai/gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello, who are you?"}]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
print(response.json()["choices"][0]["message"]["content"])

# 03_litellm_openai_agent/agent_example.py

import litellm

litellm.api_key = "your_openai_api_key"
litellm.model = "gpt-3.5-turbo"

response = litellm.completion(
    messages=[{"role": "user", "content": "What is 2 + 2?"}]
)

print(response['choices'][0]['message']['content'])
