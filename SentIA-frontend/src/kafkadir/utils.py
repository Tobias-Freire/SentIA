from confluent_kafka.admin import AdminClient

conf = {
    'bootstrap.servers': 'kafka:9093'
}

def get_topics() -> list:
    """
    Gets the list of topics from a Kafka cluster.
    """
    admin_client = AdminClient(conf)
    try:
        topics = admin_client.list_topics(timeout=10)
        return list(topics.topics.keys())
    except Exception as e:
        print(f"Failed to get topics: {e}")
        return []