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

def analyze_sentiment(text):
    stars_result = stars_pipeline(text)[0]
    stars_rank = int(stars_result["label"][0])

    emotion_result = emotion_pipeline(text)[0]
    predominant_emotion = emotion_result[0]["label"]

    sentiment_result = sentiment_pipeline(text)[0]
    general_classification = sentiment_result["label"]

    return {
        "feedback": text,
        "stars_ranking": stars_rank,
        "predominant_emotion": predominant_emotion,
        "general_classification": general_classification
    }