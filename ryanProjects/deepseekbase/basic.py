import ollama

# Create streaming completion
completion = ollama.chat(
    model="deepseek-r1:latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Why sky is blue?"}
    ],
)

# Access message content directly from response
response = completion['message']['content']

print(response)