# Portfolio 3: Transactions and Concurrency

## 1. Overview

This portfolio demonstrates transaction management, transaction isolation, and concurrency control using the West Haven Hotel database in MySQL.

The practical exercises explore how database transactions behave when changes are committed or rolled back, how separate database connections observe changes made by one another, and how MySQL manages concurrent updates to the same record.

The experiments were conducted using the `bookings` table and `booking_id = 1` to observe transaction behaviour.

## 2. Objectives

The objectives of this portfolio are to:

- Demonstrate how transactions are started and completed using `START TRANSACTION`, `COMMIT`, and `ROLLBACK`.
- Verify that committed changes persist while uncommitted changes can be rolled back.
- Examine transaction isolation using two separate database connections.
- Demonstrate concurrent updates and row-level locking.
- Document the observed database behaviour with SQL scripts and screenshots.

## 3. Tools and Environment

- **Database Management System:** MySQL
- **Database:** `west_haven_hotel`
- **Table:** `bookings`
- **Record used for testing:** `booking_id = 1`
- **Database engine:** InnoDB
- **SQL editor and project workspace:** MySQL Workbench and Visual Studio Code
- **Version control:** Git and GitHub

Two separate database connections, Connection A and Connection B, were used for the transaction isolation and concurrency experiments.

## 4. Practical Exercises

### 4.1 COMMIT Demonstration

**File:** `Rollback_and_commit.sql`

The COMMIT demonstration illustrates how a transaction can modify a booking record and permanently save the change.

The transaction was started using `START TRANSACTION`. The status of booking 1 was changed from `Checked-out` to `Cancelled`, and a `SELECT` statement was used to verify the change. The transaction was then completed using `COMMIT`.

A subsequent query confirmed that the committed status remained `Cancelled`.

**Key finding:** COMMIT makes the transaction's changes permanent, subject to the database transaction succeeding.

**Evidence:** `Oluwakeyede_Odutayo_COMMIT.png`

### 4.2 ROLLBACK Demonstration

**File:** `Rollback_and_commit.sql`

The ROLLBACK demonstration examined how an uncommitted change can be undone.

A transaction was started, and the status of booking 1 was changed from `Checked-out` to `Cancelled`. A query verified the updated status before `ROLLBACK` was executed.

A final query confirmed that the original status, `Checked-out`, had been restored.

**Key finding:** ROLLBACK reverses the changes made within the active transaction that have not been committed.

**Evidence:** `Oluwakeyede_Odutayo_ROLLBACK.png`

### 4.3 Transaction Isolation

**File:** `Transaction_Isolation.sql`

The transaction isolation experiment used two separate database connections to observe how MySQL handles uncommitted changes.

Both connections were configured to use the `REPEATABLE READ` isolation level, as verified using:

```sql
SELECT
    CONNECTION_ID() AS connection_id,
    @@transaction_isolation AS isolation_level;
```

Connection A started a transaction and updated booking 1 from `Cancelled` to `Checked-in`. A query in Connection A confirmed the change.

Before Connection A committed, Connection B queried the same booking and returned the previously committed status, `Cancelled`, rather than the uncommitted value.

Connection A then executed `COMMIT`. Connection B subsequently queried the booking again and observed the committed status, `Checked-in`.

**Key finding:** The experiment demonstrated that Connection B did not see Connection A's uncommitted change. After the change was committed, Connection B could observe the new value under the conditions used in the experiment.

**Evidence files:**
- `Connection_A.png`
- `Connection_B.png`
- `Connection_A_transaction&Query.png`
- `Connection_A_AfterCommit.png`
- `Connection_B_AfterCommit.png`

### 4.4 Concurrency Control and Row-Level Locking

**File:** `Concurrency.sql`

The concurrency experiment investigated what happens when two transactions attempt to update the same booking record concurrently.

Connection A started a transaction and updated booking 1 from `Checked-in` to `Cancelled`. The transaction remained open, leaving Connection A's update uncommitted.

While Connection A held the row lock, Connection B started a transaction and attempted to update the same record to `Checked-out`.

Connection B's update waited because Connection A held a lock on the record being modified.

Connection A then executed `COMMIT`, saving its update and releasing the lock. Connection B's waiting update subsequently completed. A query in Connection B showed the booking status as `Checked-out`.

**Key finding:** The experiment demonstrated how InnoDB row-level locking coordinates concurrent updates to the same record. Connection B had to wait for Connection A to release the conflicting lock before its update could proceed.

**Evidence files:**
- `ConnectionA_Concurrency.png`
- `ConnectionB_Concurrency.png`
- `Connection_B_Query.png`
- `ConnectionB_Concurrency_AfterCommit.png`

## 5. Summary of Results

| Experiment | Operation | Observed result |
|---|---|---|
| COMMIT | Changed booking status to `Cancelled` and committed the transaction | The change persisted |
| ROLLBACK | Changed booking status to `Cancelled` and rolled back the transaction | The original status, `Checked-out`, was restored |
| Transaction isolation | Connection A updated the booking while Connection B queried it before and after the commit | B observed the previous committed value before the commit and the new value afterwards |
| Concurrency control | Connection B attempted to update a record locked by Connection A | B's update waited until A committed, after which B's update completed |

## 6. Files and Evidence

The portfolio directory contains the following SQL scripts and supporting materials:

| File | Description |
|---|---|
| `Rollback_and_commit.sql` | SQL statements for the COMMIT and ROLLBACK demonstrations |
| `Transaction_Isolation.sql` | SQL statements for the two-connection isolation experiment |
| `Concurrency.sql` | SQL statements for the concurrent update and locking experiment |
| `Oluwakeyede_Odutayo_COMMIT.png` | Screenshot evidence for COMMIT |
| `Oluwakeyede_Odutayo_ROLLBACK.png` | Screenshot evidence for ROLLBACK |
| `Connection_A.png` | Connection A evidence |
| `Connection_B.png` | Connection B evidence |
| `Connection_A_transaction&Query.png` | Transaction and query evidence |
| `Connection_A_AfterCommit.png` | Evidence captured after Connection A committed |
| `Connection_B_AfterCommit.png` | Evidence captured after the commit |
| `ConnectionA_Concurrency.png` | Connection A concurrency evidence |
| `ConnectionB_Concurrency.png` | Connection B concurrency evidence |
| `Connection_B_Query.png` | Query evidence from Connection B |
| `ConnectionB_Concurrency_AfterCommit.png` | Evidence of Connection B after the lock was released |

The screenshots provide visual evidence of the queries and observed results, while the SQL files preserve the statements used in the experiments.

## 7. Conclusion

This portfolio provided practical experience with transaction management, isolation, and concurrency control in MySQL.

The COMMIT and ROLLBACK exercises demonstrated how transactions can preserve or undo database changes. The isolation experiment showed how separate database connections interact with committed and uncommitted data. The concurrency experiment demonstrated how row-level locking prevents conflicting updates from proceeding simultaneously on the same locked record.

Overall, the exercises highlighted the importance of transaction management and concurrency control in maintaining consistent and reliable database operations in a hotel management system.cy
