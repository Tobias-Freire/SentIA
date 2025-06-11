import os

general_conf = {'bootstrap.servers': 'kafka:9093'}
consumer_conf = {
    'bootstrap.servers': 'kafka:9093',
    'group.id': 'foo',
    'auto.offset.reset': 'smallest'
}
topics = ['feedbacks']

mongo_uri = os.getenv('mongodb_uri')
