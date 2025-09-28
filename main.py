from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

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

    search_results = tavily.search(query=request.topic, max_results=3)
    news_sources = [result["url"] for result in search_results["results"]]

    prompt = f"""
    Write a LinkedIn-style professional post summarizing recent news on: {request.topic}
    Base it on these sources: {news_sources}.
    Keep it engaging and concise.
    """

    response = model.invoke(prompt)

    return GeneratePostRequest(
        topic=request.topic,
        news_sources=news_sources,  
        linkedin_post=response.content,
        image_suggestion=None
    )




