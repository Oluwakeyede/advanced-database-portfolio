import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Retrieve MongoDB connection string
uri = os.getenv("MONGODB_URI")

# Connect to MongoDB
client = MongoClient(uri, serverSelectionTimeoutMS=10000)

try:
    client.admin.command("ping")
    print("Successfully connected to MongoDB Atlas!")

except Exception as e:
    print(f"Connection failed: {e}")

finally:
    client.close()