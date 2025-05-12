# sentiment-analysis
A project to analyze, classificate and rank sentiments in texts.

## Getting started
**Pre-requisites**: have python and pip installed.
- Step 1: Create a virtual environment to isolate dependencies (`python3 -m venv venv`)
- Step 2: Activate the virtual environment (`source venv/bin/activate`)
- Step 3: Install the dependencies (`pip install -r requirements.txt`)

### How to run the API
- Run the API with fastapi (`fastapi dev app.py`), or directly with uvicorn (`uvicorn app:app --reload`)
- Now you can use the API by making POST requests to http://localhost:8000/analyze_sentiment, sending a JSON body like:
  ```json
  {
    "text": "your feedback here"
  }
  ```
- Example request using curl:
  ```bash
  curl -X POST "http://localhost:8000/analyze_sentiment" -H "Content-Type: application/json" -d '{"text": "This is a great product!"}'
  ```
- Example response:
  ```json
  {
    "label": "5 stars",
    "score": 0.7255880236625671
  }
  ```

### How to run the tests
- Run the command `pytest tests/tests.py`