from fastapi import APIRouter
from pydantic import BaseModel
from src.analysis import analyze_sentiment

router = APIRouter()

class SentimentRequest(BaseModel):
    text: str

@router.post("/analyze_sentiment")
async def sentiment_analysis(request: SentimentRequest):
    """
    Analyze the sentiment of the provided text.
    """
    result = analyze_sentiment(request.text)
    return result
