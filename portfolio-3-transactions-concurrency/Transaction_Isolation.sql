-- =====================================================
-- PORTFOLIO 3: TRANSACTIONS AND CONCURRENCY
-- Demonstration: TRANSACTION ISOLATION
-- Database: West Haven Hotel
-- =====================================================


-- =====================================================
-- CONNECTION A — STEP 1
-- Run the following in Connection A first.
-- =====================================================

USE west_haven_hotel;

-- Identify Connection A and check its isolation level
SELECT
    CONNECTION_ID() AS connection_id,
    @@transaction_isolation AS isolation_level;


-- =====================================================
-- CONNECTION A — STEP 2
-- Begin the transaction and update the booking.
-- Do NOT commit yet.
-- =====================================================

START TRANSACTION;

UPDATE bookings
SET status = 'Checked-in'
WHERE booking_id = 1;

-- Verify the change in Connection A.
-- Expected status: Checked-in

SELECT booking_id, status
FROM bookings
WHERE booking_id = 1;


-- =====================================================
-- CONNECTION B — STEP 1
-- IMPORTANT: Run this BEFORE committing in Connection A.
-- =====================================================

USE west_haven_hotel;

-- Identify Connection B and check its isolation level
SELECT
    CONNECTION_ID() AS connection_id,
    @@transaction_isolation AS isolation_level;

-- Check the booking while Connection A's update is uncommitted.
-- Expected status: Cancelled

SELECT booking_id, status
FROM bookings
WHERE booking_id = 1;


-- =====================================================
-- CONNECTION A — STEP 3
-- Return to Connection A and commit the transaction.
-- =====================================================

COMMIT;


-- =====================================================
-- CONNECTION B — STEP 2
-- Return to Connection B and run this query again.
-- =====================================================

-- Check the booking after Connection A commits.
-- Expected status: Checked-in

SELECT booking_id, status
FROM bookings
WHERE booking_id = 1;


-- =====================================================
-- END OF TRANSACTION ISOLATION DEMONSTRATION
-- =====================================================
