
USE west_haven_hotel;

-- Query 1: Retrieve bookings with guest details
SELECT
    b.booking_id,
    g.full_name,
    g.phone,
    b.check_in_date,
    b.check_out_date,
    b.status
FROM bookings AS b
JOIN guests AS g
    ON b.guest_id = g.guest_id
ORDER BY b.check_in_date;

-- Query 2: Calculate total payments received per booking
SELECT
    b.booking_id,
    g.full_name,
    COALESCE(SUM(p.amount), 0) AS total_paid
FROM bookings AS b
JOIN guests AS g
    ON b.guest_id = g.guest_id
LEFT JOIN payments AS p
    ON b.booking_id = p.booking_id
GROUP BY b.booking_id, g.full_name
ORDER BY total_paid DESC;

-- Query 3: Summarise bookings by status
SELECT
    status,
    COUNT(*) AS total_bookings
FROM bookings
GROUP BY status
ORDER BY total_bookings DESC;
