USE west_haven_hotel;

SELECT 'room_types' AS table_name, COUNT(*) AS row_count FROM room_types
UNION ALL
SELECT 'rooms', COUNT(*) FROM rooms
UNION ALL
SELECT 'staff', COUNT(*) FROM staff
UNION ALL
SELECT 'staff_shifts', COUNT(*) FROM staff_shifts
UNION ALL
SELECT 'guests', COUNT(*) FROM guests
UNION ALL
SELECT 'bookings', COUNT(*) FROM bookings
UNION ALL
SELECT 'booking_rooms', COUNT(*) FROM booking_rooms
UNION ALL
SELECT 'payments', COUNT(*) FROM payments;