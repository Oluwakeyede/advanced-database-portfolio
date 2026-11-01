# Portfolio 4: NoSQL and Advanced Data Models

## 1. Project Overview

This portfolio demonstrates the implementation of a NoSQL database using **MongoDB** for the West Haven Hotel & Suites reservation system.

The project uses MongoDB's document-oriented data model to store hotel booking information, including guest details, booking information, room details, staff information and payment records.

The objective was to demonstrate how a relational database structure can be adapted into a flexible NoSQL document model.

## 2. Database Setup and Connection

A MongoDB Atlas cloud cluster named `WestHavenCluster` was created for the project.

The database is named `west_haven_hotel`, with a collection named `bookings`.

Python was used to connect to MongoDB through PyMongo. The connection credentials were stored in an environment variable using a `.env` file to avoid exposing sensitive connection information.

**Tools and technologies:**
- MongoDB Atlas
- Python
- PyMongo
- python-dotenv

## 3. NoSQL Document Model

The original hotel database was designed using MySQL, with separate relational tables for guests, bookings, rooms, room types, staff and payments.

For the MongoDB implementation, related information was embedded within booking documents.

Each booking document contains:

- `booking_id`: Unique booking identifier.
- `booking`: Booking dates, status and assigned staff information.
- `guest`: Guest identification and contact information.
- `rooms`: An array containing room details and rates.
- `payments`: An array containing payment records.

This structure uses nested documents and embedded arrays to represent related hotel information within a single booking document.

## 4. Data Migration

A Python script (`import_bookings.py`) was developed to read the existing MySQL seed data and transform the relational records into MongoDB documents.

The script combines related records, constructs the document structure and imports the resulting documents into the MongoDB collection.

The import was completed successfully.

**Migration result:**
- Source booking records processed: 40
- Documents imported into MongoDB: 40

The import script uses an upsert operation based on `booking_id`, allowing existing documents to be replaced rather than duplicated when the import is run again.

## 5. CRUD Operations

CRUD operations were implemented using PyMongo in `crud_test.py`.

The exercise demonstrated:

- **Create:** Insert a new test document using `insert_one()`.
- **Read:** Retrieve a document using `find_one()`.
- **Update:** Modify a document using `update_one()` and the `$set` operator.
- **Delete:** Remove a document using `delete_one()`.

A separate `crud_test` collection was used to prevent changes to the original hotel booking records.

The test was successful, and the original bookings collection remained intact with 40 documents.

## 6. Queries and Filtering

The `query_bookings.py` script demonstrates how to retrieve specific booking information using MongoDB queries.

The queries include:

- Retrieving bookings by booking status.
- Finding bookings belonging to a particular guest.
- Filtering bookings by room type.
- Finding bookings containing payment records above a specified amount.

Dot notation was used to access fields inside embedded documents and arrays. Comparison operators such as `$gt` were also demonstrated.

## 7. Aggregation

The `aggregation.py` script demonstrates MongoDB aggregation pipelines for analysing booking information.

Three aggregation exercises were implemented:

1. Grouping bookings by status and counting the number of bookings in each group.
2. Calculating total payments grouped by payment method.
3. Grouping bookings by room type and counting the records in each group.

The implementation demonstrates the use of aggregation operators including `$group`, `$sum`, `$unwind` and `$sort`.

## 8. Indexing

The `indexing.py` script demonstrates indexing in MongoDB.

A unique ascending index was created on the `booking_id` field.

This supports efficient retrieval using the booking identifier and prevents duplicate booking IDs from being inserted into the collection.

## 9. Suitability of the Document Model

The document-oriented model is suitable for the West Haven Hotel reservation system because booking information is frequently accessed alongside related guest, room and payment details.

Embedding related information within booking documents allows the hotel to retrieve much of the information required for a booking through a single document query.

The model also provides flexibility when storing related information that may vary between bookings, particularly payment records.

However, embedding introduces some data duplication and requires care when updating repeated information. The design is therefore most appropriate where related information is commonly accessed together and embedded arrays remain manageable.

## 10. Conclusion

This portfolio demonstrates the practical implementation of MongoDB as a NoSQL database for the West Haven Hotel & Suites reservation system.

The work covered MongoDB Atlas setup, Python connectivity, migration from MySQL, document modelling, CRUD operations, querying, aggregation and indexing.

The exercise provided practical experience in working with document-oriented data structures and understanding how NoSQL databases can support real-world business applications.

