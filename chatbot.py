import requests

def get_response(query):
    prompt = f"""
You are a helpful AI assistant.
Give clear, correct and simple answers.

Question: {query}
Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]