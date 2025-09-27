from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

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
    return GeneratePostRequest(
        topic=request.topic,
        news_sources=[],
        linkedin_post=f"Draft: Latest on {request.topic} — summary will go here.",
        image_suggestion=None
    )