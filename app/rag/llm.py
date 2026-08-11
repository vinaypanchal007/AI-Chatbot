import os
from groq import AsyncGroq

client = AsyncGroq(
    api_key = os.environ.get("GROQ_API_KEY")
)

async def generate_response(prompt: str) -> str:
    
    response = await client.chat.completion.create(
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