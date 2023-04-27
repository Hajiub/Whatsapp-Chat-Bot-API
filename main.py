from fastapi import FastAPI
from pydantic import BaseModel, validator
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import uvicorn
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class Question(BaseModel):
    question: str

def generate_answer(question: str) -> str:
    model_engine = "text-davinci-003"
    prompt = f"Q: {question}\nA:"

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer

app = FastAPI()

@app.post("/")
async def get_answer(question: Question) -> str:
    question = question.question.strip()
    answer = generate_answer(question)
    bot_res = MessagingResponse()
    msg = bot_res.message()
    msg.body(answer)
    return str(bot_res)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
