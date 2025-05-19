from pymongo import MongoClient 
    
class MongoService:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.collection = self.client['sentia']['feedback_analysis']

    def insert_data(self, data):
        try:
            result = self.collection.insert_one(data)
            if result.acknowledged:
                return {
                    "code": 200, 
                    "message": "Data inserted successfully", 
                    "inserted_id": str(result.inserted_id)
                }
            else:
                raise Exception("Data insertion failed")
        except Exception as e:
            return {
                "code": 500, 
                "message": str(e)
            }