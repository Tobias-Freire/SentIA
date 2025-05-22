import concurrent.futures
from functools import lru_cache
from transformers import pipeline
from torch import cuda

device = 0 if cuda.is_available() else -1

stars_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
    device=device
)
emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1,
    device=device
)
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    device=device
)

def process_stars(text):
    result = stars_pipeline(text)[0]
    return int(result["label"][0])

def process_emotion(text):
    result = emotion_pipeline(text)[0]
    return result[0]["label"]

def process_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result["label"]

@lru_cache(maxsize=128) 
def analyze_sentiment(text):
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            stars_future = executor.submit(process_stars, text)
            emotion_future = executor.submit(process_emotion, text)
            sentiment_future = executor.submit(process_sentiment, text)

            stars_rank = stars_future.result()
            predominant_emotion = emotion_future.result()
            general_classification = sentiment_future.result()

            return {
                "feedback": text,
                "stars_rank": stars_rank,
                "predominant_emotion": predominant_emotion,
                "general_classification": general_classification
            }
    except Exception as e:
        return {
            "feedback": text,
            "error": str(e),
            "status": "failed",
            "code": 500
        }