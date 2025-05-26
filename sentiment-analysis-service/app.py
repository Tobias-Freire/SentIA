from fastapi import FastAPI
from contextlib import asynccontextmanager
from threading import Thread
from src.routes import router
from src.consumer import consume_messages
from src.configuration import general_conf
from confluent_kafka.admin import AdminClient, NewTopic

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create Kafka topic
    admin_client = AdminClient(general_conf)
    topic_name = "feedbacks"
    topic = NewTopic(topic_name, num_partitions=1, replication_factor=1)
    result_dict = admin_client.create_topics([topic])
    for topic, result in result_dict.items():
        try:
            result.result()
            print(f"Topic {topic} created")
        except Exception as e:
            print(f"Failed to create topic {topic}: {e}")
    
    # Start the consumer thread
    consumer_thread = Thread(target=consume_messages, daemon=True)
    consumer_thread.start()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)