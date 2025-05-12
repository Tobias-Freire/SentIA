"""
Sentiment Analysis Package
Version: 1.0.0
"""

from .routes import router
from .analysis import analyze_sentiment

__version__ = "1.0.0"
__all__ = ["router", "analyze_sentiment"]