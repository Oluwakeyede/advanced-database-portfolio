import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["west_haven_hotel"]
bookings = db["bookings"]

try:
    sample = bookings.find_one()
    pprint(sample)
finally:
    client.close()