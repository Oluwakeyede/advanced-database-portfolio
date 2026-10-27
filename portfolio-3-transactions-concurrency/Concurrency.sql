-- =====================================================
-- PORTFOLIO 3: TRANSACTIONS AND CONCURRENCY
-- Demonstration: CONCURRENT TRANSACTIONS AND ROW LOCKING
-- Database: West Haven Hotel
-- =====================================================


-- =====================================================
-- CONNECTION A — STEP 1
-- Execute these queries first in Connection A.
-- =====================================================

USE west_haven_hotel;

-- Begin a transaction
START TRANSACTION;

-- Update booking 1 and acquire a lock on the row
UPDATE bookings
SET status = 'Cancelled'
WHERE booking_id = 1;

-- Verify the change within Connection A
-- Expected status: Cancelled

SELECT booking_id, status
FROM bookings
WHERE booking_id = 1;


-- IMPORTANT:
-- Leave this transaction open.
-- Do NOT execute COMMIT yet.


-- =====================================================
-- CONNECTION B — STEP 1
-- Execute these queries in Connection B while A's
-- transaction is still open.
-- =====================================================

USE west_haven_hotel;

-- Begin a transaction
START TRANSACTION;

-- Attempt to update the same booking record
-- This query should wait while Connection A holds
-- the lock on booking_id = 1.

UPDATE bookings
SET status = 'Checked-out'
WHERE booking_id = 1;


-- =====================================================
-- CONNECTION A — STEP 2
-- While Connection B's UPDATE is waiting,
-- return to Connection A and execute:
-- =====================================================

COMMIT;

-- Purpose:
-- Commit Connection A's change and release its row lock.


-- =====================================================
-- CONNECTION B — STEP 2
-- After Connection B's UPDATE finishes, execute:
-- =====================================================

SELECT booking_id, status
FROM bookings
WHERE booking_id = 1;

-- Expected status: Checked-out


-- =====================================================
-- END OF CONCURRENCY DEMONSTRATION
-- =====================================================
