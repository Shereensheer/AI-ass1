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
