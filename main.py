from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Message(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "AI server is running 🚀"}

@app.post("/chat")
def chat(msg: Message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Ты полезный ИИ помощник"},
            {"role": "user", "content": msg.text}
        ]
    )

    return {
        "answer": response.choices[0].message.content
    }
