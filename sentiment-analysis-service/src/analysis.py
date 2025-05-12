from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
def analyze_sentiment(text):
    return sentiment_pipeline(text)