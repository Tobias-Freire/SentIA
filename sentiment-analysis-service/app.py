from fastapi import FastAPI
from contextlib import asynccontextmanager
from threading import Thread
from src.routes import router
from src.consumer import consume_messages

@asynccontextmanager
async def lifespan(app: FastAPI):
    consumer_thread = Thread(target=consume_messages, daemon=True)
    consumer_thread.start()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)