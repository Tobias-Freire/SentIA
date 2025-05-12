from confluent_kafka import Producer
import json

def send_message(topic: str, key: str, value) -> dict:
    """
    Sends a message to a Kafka topic.

    :param topic: The Kafka topic to send the message to.
    :param key: The key for the message.
    :param value: The value of the message.
    """
    conf = {
        'bootstrap.servers': 'kafka:9093',
        'client.id': 'python-producer'
    }
    producer = Producer(conf)

    try:
        producer.produce(topic, key=key, value=json.dumps(value))
        producer.flush()
        return {"status_code": 200, "status_message": "Message sent successfully"}
    except Exception as e:
        return {"status_code": 500, "status_message": f"Failed to send message: {str(e)}"}