import sqlite3
import openai
import os
from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv("YOUR_API_KEY")

connection = sqlite3.connect("database/data_lux.db")
cursor = connection.cursor()

question = input("Ask a question about the emails: ")

prompt = f"""
You are an assistant analyzing a database of emails with columns:
sender, subject, body, date, sentiment, email_type.
The user asked: "{question}"
Return a Python snippet that counts or filters emails and outputs the answer as text.
"""

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=150,
    temperature=0
)

print("GPT Suggestion / Answer:")
print(response.choices[0].text.strip())