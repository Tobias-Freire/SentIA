from src.analysis import analyze_sentiment

def test_positive_sentiment():
    pos_feedback = "This is a great product! I love it."
    result = analyze_sentiment(pos_feedback)[0]
    assert result["label"] == "5 stars" or result["label"] == "4 stars"

def test_negative_sentiment():
    neg_feedback = "This is the worst product I have ever used. I'm very disappointed."
    result = analyze_sentiment(neg_feedback)[0]
    assert result["label"] == "1 star" or result["label"] == "2 stars"

def test_neutral_sentiment():
    neutral_feedback = "O produto é ok, nada de especial."
    result = analyze_sentiment(neutral_feedback)[0]
    assert result["label"] == "3 stars"