
import os
import re
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv
from pymongo import MongoClient


# --------------------------------------------------
# 1. LOAD CONFIGURATION
# --------------------------------------------------

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found in .env file")

BASE_DIR = Path(__file__).resolve().parent

SEED_FILE = (
    BASE_DIR.parent
    / "portfolio-1-database-design"
    / "seed_data.sql"
)

if not SEED_FILE.exists():
    raise FileNotFoundError(f"Seed file not found: {SEED_FILE}")


# --------------------------------------------------
# 2. PARSE SQL SEED DATA
# --------------------------------------------------

def split_sql_values(text):
    """Split SQL values while respecting quoted strings."""
    values = []
    current = []
    in_quote = False

    i = 0

    while i < len(text):
        char = text[i]

        if char == "'":
            if in_quote and i + 1 < len(text) and text[i + 1] == "'":
                current.extend(["'", "'"])
                i += 2
                continue

            in_quote = not in_quote

        if char == "," and not in_quote:
            values.append("".join(current).strip())
            current = []
        else:
            current.append(char)

        i += 1

    if current:
        values.append("".join(current).strip())

    return values


def parse_value(value):
    """Convert SQL literals into Python values."""
    value = value.strip()

    if value.upper() == "NULL":
        return None

    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")

    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def extract_rows(values_text):
    """Extract individual SQL value tuples."""
    rows = []
    current = []
    depth = 0
    in_quote = False

    i = 0

    while i < len(values_text):
        char = values_text[i]

        if char == "'":
            if in_quote and i + 1 < len(values_text) and values_text[i + 1] == "'":
                current.extend(["'", "'"])
                i += 2
                continue

            in_quote = not in_quote

        if not in_quote:
            if char == "(":
                if depth == 0:
                    current = []
                else:
                    current.append(char)
                depth += 1

            elif char == ")":
                depth -= 1

                if depth == 0:
                    fields = split_sql_values("".join(current))
                    rows.append([parse_value(v) for v in fields])
                else:
                    current.append(char)

            elif depth > 0:
                current.append(char)

        else:
            current.append(char)

        i += 1

    return rows


def load_seed_data(file_path):
    """Read INSERT statements and return table records."""
    sql = file_path.read_text(encoding="utf-8")

    pattern = re.compile(
        r"INSERT INTO\s+(\w+)\s*\((.*?)\)\s*VALUES\s*(.*?);",
        re.IGNORECASE | re.DOTALL
    )

    tables = {}

    for match in pattern.finditer(sql):
        table_name = match.group(1).lower()

        columns = [
            column.strip().strip("`")
            for column in match.group(2).split(",")
        ]

        rows = extract_rows(match.group(3))

        tables[table_name] = [
            dict(zip(columns, row))
            for row in rows
        ]

    return tables


# --------------------------------------------------
# 3. LOAD RELATIONAL TABLES
# --------------------------------------------------

tables = load_seed_data(SEED_FILE)

guests = {
    row["guest_id"]: row
    for row in tables["guests"]
}

staff = {
    row["staff_id"]: row
    for row in tables["staff"]
}

rooms = {
    row["room_id"]: row
    for row in tables["rooms"]
}

room_types = {
    row["room_type_id"]: row
    for row in tables["room_types"]
}

booking_rooms = tables["booking_rooms"]

payments = tables["payments"]


# --------------------------------------------------
# 4. TRANSFORM BOOKINGS INTO DOCUMENTS
# --------------------------------------------------

def convert_date(value):
    if value is None:
        return None

    return datetime.fromisoformat(str(value))


documents = []

for booking in tables["bookings"]:

    booking_id = booking["booking_id"]

    guest = guests[booking["guest_id"]]
    assigned_staff = staff[booking["staff_id"]]

    # Find all rooms associated with this booking
    assigned_rooms = []

    for booking_room in booking_rooms:
        if booking_room["booking_id"] == booking_id:

            room = rooms[booking_room["room_id"]]

            room_type = room_types[room["room_type_id"]]

            assigned_rooms.append({
                "room_id": room["room_id"],
                "room_number": room["room_number"],
                "room_status": room["status"],
                "room_type": room_type["type_name"],
                "nightly_rate": room_type["nightly_rate"],
                "max_guests": room_type["max_guests"],
                "rate_charged": booking_room["rate_charged"]
            })

    # Find payment records for this booking
    booking_payments = []

    for payment in payments:
        if payment["booking_id"] == booking_id:

            booking_payments.append({
                "payment_id": payment["payment_id"],
                "amount": payment["amount"],
                "method": payment["method"],
                "paid_at": convert_date(payment["paid_at"])
            })

    document = {
        "booking_id": booking_id,

        "guest": {
            "guest_id": guest["guest_id"],
            "full_name": guest["full_name"],
            "phone": guest["phone"],
            "email": guest["email"]
        },

        "booking": {
            "staff": {
                "staff_id": assigned_staff["staff_id"],
                "full_name": assigned_staff["full_name"],
                "role": assigned_staff["role"]
            },
            "check_in_date": convert_date(booking["check_in_date"]),
            "check_out_date": convert_date(booking["check_out_date"]),
            "status": booking["status"]
        },

        "rooms": assigned_rooms,

        "payments": booking_payments
    }

    documents.append(document)


# --------------------------------------------------
# 5. INSERT DOCUMENTS INTO MONGODB ATLAS
# --------------------------------------------------

client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=10000
)

try:
    client.admin.command("ping")

    db = client["west_haven_hotel"]
    collection = db["bookings"]

    # Upsert prevents duplicate booking IDs when rerunning
    for document in documents:
        collection.replace_one(
            {"booking_id": document["booking_id"]},
            document,
            upsert=True
        )

    print("MongoDB import completed successfully!")
    print(f"Bookings processed: {len(documents)}")
    print(f"Documents in collection: {collection.count_documents({})}")

except Exception as error:
    print(f"Import failed: {error}")
    raise

finally:
    client.close()
