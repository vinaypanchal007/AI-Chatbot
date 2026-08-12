import os
from dotenv import load_dotenv
from groq import AsyncGroq

load_dotenv()

client = AsyncGroq(
    api_key = os.environ.get("GROQ_API_KEY")
)

async def generate_response(prompt: str) -> str:
    
    response = await client.chat.completions.create(
        model = os.environ.get("GROQ_MODEL"),
        messages = [
            {
                "role" : "system",
                "content" : "You are a helpful assistant."
            },
            {
                "role" : "user",
                "content" : prompt
            }
        ]
    )
    
    return response.choices[0].message.content