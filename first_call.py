from google import genai

client = genai.Client()

response = client.interactions.create(
    model="gemini-3.8-flash",
    input="用一句话解释什么是 RAG",
)

print(response.output_text)
