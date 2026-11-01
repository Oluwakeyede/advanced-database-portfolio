
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["west_haven_hotel"]
bookings = db["bookings"]

try:
    # 1. Count bookings by status
    print("\n1. BOOKINGS BY STATUS")

    status_pipeline = [
        {
            "$group": {
                "_id": "$booking.status",
                "total_bookings": {"$sum": 1}
            }
        },
        {"$sort": {"total_bookings": -1}}
    ]

    pprint(list(bookings.aggregate(status_pipeline)))

    # 2. Calculate revenue by payment method
    print("\n2. REVENUE BY PAYMENT METHOD")

    payment_pipeline = [
        {"$unwind": "$payments"},
        {
            "$group": {
                "_id": "$payments.method",
                "total_revenue": {"$sum": "$payments.amount"}
            }
        },
        {"$sort": {"total_revenue": -1}}
    ]

    pprint(list(bookings.aggregate(payment_pipeline)))

    # 3. Count bookings by room type
    print("\n3. BOOKINGS BY ROOM TYPE")

    room_pipeline = [
        {"$unwind": "$rooms"},
        {
            "$group": {
                "_id": "$rooms.room_type",
                "total_bookings": {"$sum": 1}
            }
        },
        {"$sort": {"total_bookings": -1}}
    ]

    pprint(list(bookings.aggregate(room_pipeline)))

finally:
    client.close()
