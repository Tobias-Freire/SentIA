const producer_config = {
    'bootstrap.servers': 'kafka:9093',
    'acks': 'all',
    'dr_msg_cb': true
}

const consumer_config = {
    'bootstrap.servers': 'kafka:9093',
    'group.id': 'sentia-group',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': false
}

export default producer_config