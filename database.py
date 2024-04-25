
from pymongo import MongoClient
from pymongo.database import Database

db: Database = MongoClient(f"mongodb+srv://fedislimen98:iM0m5zxIipJ0iKZ3@cluster0.hsxojrp.mongodb.net/")["app_db"]