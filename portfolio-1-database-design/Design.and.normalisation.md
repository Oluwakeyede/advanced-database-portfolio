## Design
The database has eight tables: `guests`, `room_types`, `rooms`, `staff`,
`staff_shifts`, `bookings`, `booking_rooms` and `payments`.

- One guest makes many bookings, and one staff member handles many bookings.
- A booking can include several rooms, so `booking_rooms` links `bookings` and
  `rooms` (a many-to-many relationship).
- One room type has many rooms, and one booking has many payments.

**Keys and constraints.** Every table has an auto-incrementing primary key.
Foreign keys link the tables. `NOT NULL` is used on required columns, `UNIQUE` on
`room_number`, `type_name` and `shift_date` (one staff member per day), and
`UNIQUE (booking_id, room_id)` stops a room being added twice to one booking.
`CHECK` constraints reject bad data, such as a check-out date on or before the
check-in date, or a rate or amount of zero or less.

## Normalisation
Normalisation is organising tables and their relationships to reduce repeated
data and avoid anomalies when inserting, updating or deleting records.

**1NF (atomic values).** Every cell holds one value. A booking can cover several
rooms, so rooms are not stored as a list inside `bookings`. The link table
`booking_rooms` has one row per room in a booking.

**2NF (no partial dependency).** Every non-key column depends on the whole key.
Guest details depend on the booking and not on each room in it, so they live in
`guests`, and `bookings` holds only `guest_id`. A guest's name is updated in
one place.

**3NF (no transitive dependency).** Non-key columns depend only on the key. The
room type name and nightly rate belong to the room type and not to each room,
so they are stored once in `room_types`, and `rooms` holds only `room_type_id`.

**Design choice.** `rate_charged` is stored in `booking_rooms` on purpose. It
records the price at the time of booking, so later rate changes in `room_types`
do not change old bookings.

All eight tables meet 1NF, 2NF and 3NF.