import sys
from confluent_kafka import Consumer, KafkaError
from ..analysis import analyze_sentiment

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'foo',
    'auto.offset.reset': 'smallest'
}
consumer = Consumer(conf)

def consume_messages(consumer, topics):
    try:
        consumer.subscribe(topics)
        while True:
            msg = consumer.poll(1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaError(msg.error())
            else:
                msg_process = analyze_sentiment(msg.value().decode('utf-8'))
                print(f"Received message: {msg.value().decode('utf-8')}")
                print(f"Processed message: {msg_process}")
    finally:
        consumer.close()

consume_messages(consumer, ['feedbacks'])
