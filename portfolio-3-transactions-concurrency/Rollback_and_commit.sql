SET autocommit = 0;

-- =====================================================
-- PORTFOLIO 3: TRANSACTIONS AND CONCURRENCY
-- Demonstration: ROLLBACK
-- Database: West Haven Hotel
-- =====================================================

START TRANSACTION;

-- Change the booking status
UPDATE bookings
SET status = 'Cancelled'
WHERE booking_id = 1;

-- Verify the change before rollback
SELECT booking_id, status
FROM bookings
WHERE booking_id = 1;

-- Undo the uncommitted change
ROLLBACK;

-- Verify that the original status is restored
SELECT booking_id, status
FROM bookings
WHERE booking_id = 1;

-- =====================================================
-- PORTFOLIO 3: TRANSACTIONS AND CONCURRENCY
-- Demonstration: COMMIT
-- Database: West Haven Hotel
-- =====================================================

START TRANSACTION;

-- Change the booking status
UPDATE bookings
SET status = 'Cancelled'
WHERE booking_id = 1;

-- Verify the change before commit
SELECT booking_id, status
FROM bookings
WHERE booking_id = 1;

-- Save the change permanently
COMMIT;

-- Verify that the committed change remains
SELECT booking_id, status
FROM bookings
WHERE booking_id = 1;