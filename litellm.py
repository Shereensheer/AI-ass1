import litellm

litellm.api_key = "your_openai_api_key"
litellm.model = "gpt-3.5-turbo"

response = litellm.completion(
    messages=[{"role": "user", "content": "What is 2 + 2?"}]
)

print(response['choices'][0]['message']['content'])



