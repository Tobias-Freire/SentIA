const Kafka = require('@confluentinc/kafka-javascript');

function createProducer(config, onDeliveryReport) {
    const producer = new Kafka.Producer(config);

    return new Promise((resolve, reject) => {
        producer
            .on('ready', () => resolve(producer))
            .on('delivery-report', onDeliveryReport)
            .on('event.error', (err) => {
                console.warn('event.error', err);
                reject(err);
            });
        producer.connect();
    });
}

function produceMessage(topic, key, value, producer) {
    try {
        producer.produce(
            topic,
            -1,
            Buffer.from(value),
            key
        );
    } catch (err) {
        console.error('Error producing message:', err);
        throw err;
    }
}