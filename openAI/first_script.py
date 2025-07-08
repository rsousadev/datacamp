# Create the OpenAI client
from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv("OPEN_API_TOKEN"))

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", 
     "content": "Write a polite reply accepting an AI Engineer job offer."}]
)

print(response.choices[0].message.content)