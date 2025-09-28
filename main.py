from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

app = FastAPI()

class GeneratePostRequest(BaseModel):
    topic: str
    news_sources: List[str]
    linkedin_post: str
    image_suggestion: Optional[str] = None

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/generate-post", response_model=GeneratePostRequest)
async def generate_post(request: GeneratePostRequest):
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    prompt = f"Write a LinkedIn-style professional post summarizing recent news on: {request.topic}"

    response = model.invoke(prompt)

    return GeneratePostRequest(
        topic=request.topic,
        news_sources=[],  
        linkedin_post=response.content,
        image_suggestion=None
    )


# def test_gemini():
#     model = ChatGoogleGenerativeAI(
#         model="gemini-2.0-flash",
#         google_api_key=os.getenv("GEMINI_API_KEY")
#     )
#     response = model.invoke("Hello Gemini, can you write a 1-line greeting?")
#     print("Gemini says:", response.content)

# test_gemini()

