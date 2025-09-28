from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

load_dotenv()

app = FastAPI()

tavily_search_tool = TavilySearch(max_results=3, topic="news")

# Input model 
class GeneratePostInput(BaseModel):
    topic: str

# Output model 
class GeneratePostOutput(BaseModel):
    topic: str
    news_sources: List[str]
    linkedin_post: str
    image_suggestion: Optional[str] = None

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/generate-post", response_model=GeneratePostOutput)
async def generate_post(request: GeneratePostInput):
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    search_results = tavily_search_tool.invoke({"query": request.topic})
    news_sources = [result["url"] for result in search_results["results"]]

    prompt = f"""
    Write a LinkedIn-style professional post summarizing recent news on: {request.topic}
    Base it on these sources: {news_sources}.
    Keep it engaging and concise.
    """

    response = model.invoke(prompt)

    return GeneratePostOutput(
        topic=request.topic,
        news_sources=news_sources,
        linkedin_post=response.content,
        image_suggestion=None
    )




