import os

general_conf = {'bootstrap.servers': 'kafka:9093'}
topics = ['feedbacks']

mongo_uri = os.getenv('mongodb_uri')
