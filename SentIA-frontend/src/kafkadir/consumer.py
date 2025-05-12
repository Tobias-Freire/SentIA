from confluent_kafka import Consumer, TopicPartition
import json
from typing import Optional, Dict

def consume_latest_message(topic: str) -> Optional[Dict]:
    """
    Consumes the latest message from a Kafka topic.
    Args:
        topic (str): The Kafka topic to consume from.
    Returns:
        Optional[Dict]: The latest message as a dictionary, or None if no messages are available.
    """
    conf = {
        'bootstrap.servers': 'kafka:9093',
        'group.id': 'python-consumer',
        'enable.partition.eof': True
    }
    consumer = Consumer(conf)
    try:
        # Get topic partitions
        partitions = consumer.list_topics(topic).topics[topic].partitions
        topic_partitions = [TopicPartition(topic, p) for p in partitions]

        # Looks for the last offset in each partition
        end_offsets = consumer.get_watermark_offsets(topic_partitions[0])
        # end_offsets[1] is the last offset 
        last_offset = end_offsets[1] - 1

        if last_offset < 0:
            return None  # No messages in the topic

        # Assign the consumer to the last offset of the topic
        tp = TopicPartition(topic, 0, last_offset)
        consumer.assign([tp])

        msg = consumer.poll(1.0)
        if msg and not msg.error():
            key = msg.key().decode('utf-8') if msg.key() else None
            value = safe_deserialize(msg.value())
            return {key: value}
        return None
    except Exception as e:
        print(f"Failed to consume message: {e}")
        return None
    finally:
        consumer.close()

def safe_deserialize(x):
    if x is None:
        return None
    try:
        return json.loads(x.decode('utf-8'))
    except Exception as e:
        print(f"Failed to deserialize message: {e}")
        return None
