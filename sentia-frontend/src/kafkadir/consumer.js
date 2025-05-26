const Kafka = require('@confluentinc/kafka-javascript');

function createConsumer(config, onData) {
    const consumer = new Kafka.KafkaConsumer(config);

    return new Promise((resolve, reject) => {
        consumer
            .on('ready', () => resolve(consumer))
            .on('data', onData);
        consumer.connect();
    });
}

function consumeMessages(consumer, topic) {
    try {
        consumer.subscribe([topic]);
        consumer.consume();
    } catch (err) {
        console.error('Error consuming messages:', err);
        throw err;
    }
}