import sys
from confluent_kafka import Consumer, KafkaError
from .analysis import analyze_sentiment
from .configuration import consumer_conf, topics, mongo_uri
from .mongo import MongoService

def consume_messages():
    consumer = Consumer(consumer_conf)
    mongo_service = MongoService(mongo_uri)

    try:
        consumer.subscribe(topics)
        while True:
            msg = consumer.poll(1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                else:
                    raise KafkaError(msg.error())
            else:
                msg_process = analyze_sentiment(msg.value().decode('utf-8'))
                print(f"Processed message: {msg_process}")
                mongo_response = mongo_service.insert_data(msg_process)
                if mongo_response['code'] == 200:
                    print(f"Data inserted successfully with ID: {mongo_response['inserted_id']}")
                else:
                    print(f"Failed to insert data: {mongo_response['message']}")
    finally:
        consumer.close()
