from pymongo import MongoClient
from database.confing import MongoC, db_name

client = MongoClient(MongoC)
chicago_db = client[db_name]

Accidents = chicago_db['Accidents']