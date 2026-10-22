# Portfolio 2: Query Processing and Optimisation

## 1. Introduction

This portfolio activity explores query processing and optimisation in MySQL using the West Haven Hotel and Suites database. The objective is to understand how SQL queries retrieve data, how MySQL's query optimiser selects an execution plan, and how indexes can influence query execution.

The practical work includes executing SQL queries, examining their results, using the `EXPLAIN` statement to inspect execution plans, and comparing query plans before and after creating an index.

## 2. Case Study

West Haven Hotel and Suites is a hotel reservation system used as the case study for the Advanced Database Systems course. The database supports hotel operations involving guests, room information, bookings, payments, staff, and staff shifts.

The database contains the following tables:

- `guests`
- `rooms`
- `room_types`
- `bookings`
- `booking_rooms`
- `payments`
- `staff`
- `staff_shifts`

These tables support the retrieval and management of information needed for hotel reservation and administrative operations.

## 3. SQL Queries and Query Results

SQL queries were executed against the hotel database to retrieve relevant information and demonstrate practical database querying.

The SQL statements are maintained in `queries.sql`, while the exported query results are provided as CSV files:

- `Oluwakeyede_Odutayo_Query_1.csv`
- `Oluwakeyede_Odutayo_Query_2.csv`
- `Oluwakeyede_Odutayo_Query_3.csv`

The CSV files provide evidence of the query outputs produced during the practical exercise. Exporting the results also makes them available for further inspection using spreadsheet applications.

## 4. Query Execution Plans Using EXPLAIN

MySQL's `EXPLAIN` statement was used to inspect how the database executes a query. It provides information about the selected access method, available and chosen indexes, estimated rows examined, and additional execution details.

The following query was used to investigate guest-name retrieval:

```sql
EXPLAIN
SELECT guest_id, full_name
FROM guests
WHERE full_name = 'John Smith';
```

### Before indexing

Before creating an index on `guests.full_name`, the execution plan showed:

- **Access type:** `ALL`
- **Possible keys:** `NULL`
- **Chosen key:** `NULL`
- **Estimated rows:** 40
- **Extra:** `Using where`

The access type `ALL` indicates a full table scan. MySQL estimated that it would examine all 40 rows in the `guests` table to find records matching the specified name.

This execution plan is documented in `explain_guests_before_index.png`.

### After indexing

An index was created on the `full_name` column using the following statement:

```sql
CREATE INDEX idx_guests_full_name
ON guests(full_name);
```

The same `EXPLAIN` query was executed again after the index was created. The subsequent execution plan showed the index being used for the guest-name query.

This demonstrates how an index can provide MySQL with an alternative access path when retrieving records based on a column used in a filtering condition.

The resulting execution plan is documented in `explain_guests_after_index.png`.

## 5. Indexing and Optimisation

A database index is an auxiliary data structure that helps the database locate records without necessarily scanning every row in a table. Indexes can improve retrieval efficiency for suitable queries, particularly when indexed columns are frequently used in filtering, joining, or sorting operations.

For this experiment, `idx_guests_full_name` was created on the `guests.full_name` column.

The before-index execution plan showed a full table scan with no index selected. After the index was created, MySQL selected the new index for the query. This demonstrates a change in the query's access plan.

The SQL scripts `EXPLAIN.sql` and `INDEX.sql` contain the execution-plan and indexing statements used in the practical.

However, indexes also have costs. They require storage and may increase the work required for insertions, updates, and deletions. Consequently, indexes should be selected according to query patterns and database requirements rather than added indiscriminately to every column.

## 6. Performance Analysis

The execution-plan comparison demonstrates a change in how MySQL accesses the `guests` table.

Before indexing, the query used a full table scan and estimated that it would examine 40 rows. After indexing, MySQL selected `idx_guests_full_name` as the access path for the query.

This suggests that the index can help MySQL locate matching guest records without relying on the same full-table-scan approach. The experiment illustrates the importance of examining execution plans when investigating query optimisation.

The `rows` value reported by `EXPLAIN` is an estimate of the rows MySQL expects to examine; it is not a measurement of execution time. No measured runtime improvement is claimed in this portfolio. Actual performance gains would need to be evaluated using execution-time measurements or appropriate runtime analysis.

## 7. Evidence and Repository Files

The following files support the practical work:

| File | Purpose |
|---|---|
| `queries.sql` | SQL queries used in the portfolio activity |
| `EXPLAIN.sql` | SQL statements used to inspect execution plans |
| `INDEX.sql` | SQL statement used to create the guest-name index |
| `Oluwakeyede_Odutayo_Query_1.csv` | Exported query results |
| `Oluwakeyede_Odutayo_Query_2.csv` | Exported query results |
| `Oluwakeyede_Odutayo_Query_3.csv` | Exported query results |
| `explain_guests_before_index.png` | Execution plan before indexing |
| `explain_guests_after_index.png` | Execution plan after indexing |
| `Schema_verification.png` | Evidence of database schema verification |
| `verification_queries.sql` | SQL statements used for schema verification |

## 8. Conclusion

This practical exercise demonstrates the use of SQL queries, query-result exports, execution-plan inspection, and indexing in a MySQL hotel reservation database.

The guest-name indexing experiment showed that MySQL's execution plan changed from a full table scan to using the newly created index. It reinforced the importance of understanding execution plans when investigating query performance and selecting appropriate indexes.

The work also highlights the need to interpret optimiser estimates carefully and distinguish changes in execution plans from measured improvements in actual query execution time.