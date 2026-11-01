
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGODB_URI")
client = MongoClient(uri, serverSelectionTimeoutMS=10000)

db = client["west_haven_hotel"]
collection = db["crud_test"]

try:
    # CREATE
    test_document = {
        "test_id": "CRUD-001",
        "guest_name": "Test Guest",
        "booking_status": "Pending"
    }

    collection.insert_one(test_document)
    print("CREATE: Document inserted successfully.")

    # READ
    result = collection.find_one({"test_id": "CRUD-001"})
    print("READ:", result)

    # UPDATE
    collection.update_one(
        {"test_id": "CRUD-001"},
        {"$set": {"booking_status": "Confirmed"}}
    )

    updated = collection.find_one({"test_id": "CRUD-001"})
    print("UPDATE:", updated)

    # DELETE
    collection.delete_one({"test_id": "CRUD-001"})
    print("DELETE: Test document deleted successfully.")

    # Verify main collection remains intact
    bookings = db["bookings"]
    print("Main booking documents:", bookings.count_documents({}))

finally:
    client.close()