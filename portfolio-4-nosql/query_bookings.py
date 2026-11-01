
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["west_haven_hotel"]
bookings = db["bookings"]

try:
    # 1. Find all checked-out bookings
    print("\n1. CHECKED-OUT BOOKINGS")
    for doc in bookings.find({"booking.status": "Checked-out"}):
        print(doc["booking_id"], doc["guest"]["full_name"])

    # 2. Find bookings for a particular guest
    print("\n2. BOOKINGS FOR AMARA EZE")
    for doc in bookings.find({"guest.full_name": "Amara Eze"}):
        pprint(doc)

    # 3. Find bookings containing a particular room type
    print("\n3. KINGS ROOM BOOKINGS")
    for doc in bookings.find({"rooms.room_type": "Kings"}):
        print(doc["booking_id"], doc["guest"]["full_name"])

    # 4. Find bookings with payments above ₦40,000
    print("\n4. PAYMENTS ABOVE ₦40,000")
    for doc in bookings.find({"payments.amount": {"$gt": 40000}}):
        print(doc["booking_id"], doc["guest"]["full_name"])

finally:
    client.close()
