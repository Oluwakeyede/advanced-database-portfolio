
import os
from dotenv import load_dotenv
from pymongo import MongoClient, ASCENDING

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["west_haven_hotel"]
bookings = db["bookings"]

try:
    # Create an index on booking_id
    result = bookings.create_index(
        [("booking_id", ASCENDING)],
        unique=True
    )

    print("Index created:", result)

    # Display available indexes
    print("\nAvailable indexes:")
    for index in bookings.list_indexes():
        print(index)

finally:
    client.close()
