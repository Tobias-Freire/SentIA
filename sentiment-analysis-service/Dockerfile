FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH

COPY ./src ./src
COPY app.py .

RUN mkdir -p /root/.cache/huggingface

ENV TRANSFORMERS_CACHE=/root/.cache/huggingface

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]