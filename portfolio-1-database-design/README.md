# Portfolio 1: Database Design and Modelling

## Case study
**Organisation:** West Haven Hotel and Suites, a small hotel. The way the hotel
works is real, but all data in this repository is simulated.

**Nature of the system:** a hotel reservation and front desk system covering
bookings, room availability, check-in and check-out, and payments.

**Users of the database:** front desk staff who take bookings, the hotel
manager, and the accountant. Guests book by phone or in person.

**Major data stored:** guests, room types and rates, rooms, bookings, the rooms
in each booking, payments, and front desk staff and their shifts.

**Key operations:** reserve one or more rooms, check availability for a date
range, cancel a booking, check in and check out, record a payment, and report
on daily revenue and occupancy.

**Scope note:** staff records cover only the front desk staff who handle
bookings. The hotel has two such staff who work on alternating days, so each
date has exactly one staff member on duty.

## Files in this folder
| File | What it is |
|---|---|
| ADS_CA_ER_Diagram.png | ER diagram of the design |
| schema.sql | MySQL script that creates the database, tables, keys and constraints |
| ADS_CA_Schema.png | Evidence that all eight tables were created |