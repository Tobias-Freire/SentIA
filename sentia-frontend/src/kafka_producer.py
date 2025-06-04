from confluent_kafka import Producer
from src.config import general_conf

def create_producer():
    """
    Create a Kafka producer with the specified configuration.
    """
    producer = Producer(general_conf)
    return producer

def send_message(producer, topic, message):
    """
    Send a message to the specified Kafka topic.

    :param producer: The Kafka producer instance.
    :param topic: The topic to which the message will be sent.
    :param message: The message to send.
    """
    try:
        producer.produce(topic, value=message)
        producer.flush()
        print(f"Message sent to topic {topic}: {message}")
    except Exception as e:
        print(f"Failed to send message: {e}")