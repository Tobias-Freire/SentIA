from fastapi import APIRouter
from pydantic import BaseModel
from src.analysis import analyze_sentiment
from concurrent.futures import ThreadPoolExecutor
import asyncio

router = APIRouter()
executor = ThreadPoolExecutor(max_workers=4)

class SentimentRequest(BaseModel):
    text: str

@router.post("/analyze_sentiment")
async def sentiment_analysis(request: SentimentRequest):
    """
    Analyze the sentiment of the provided text.
    """
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(
        executor,   
        analyze_sentiment, 
        request.text
    )
    return result
