import os

general_conf = {'bootstrap.servers': 'kafka:9093'}
topics = ['feedbacks']

mongo_username = os.getenv('MONGO_USERNAME')
mongo_password = os.getenv('MONGO_PASSWORD')
mongo_uri = f"mongodb://{mongo_username}:{mongo_password}@mongodb:27017/sentia?authSource=admin"
