# MIT 8103 Advanced Database Systems
## Individual Practical Database Portfolio (CA, September Cohort 2026)

**Student:** Oluwakeyede Odutayo  
**Student ID:** 301907379 
**Course:** MIT 8103 Advanced Database Systems  
**GitHub Repository:** https://github.com/Oluwakeyede/advanced-database-portfolio 

## CASE STUDY

West Haven Hotel and Suites, a hotel reservation system. The scenario is based on a real hotel's way of working, but all data in this repository is simulated. No real guest information is stored here.

The same case study is used across all five portfolio activities.

## FILES IN THIS FOLDER

- `Odutayo_Oluwakeyede_STUDENTID_Documentation.pdf` – 2 to 3-page portfolio documentation.
- `Odutayo_Oluwakeyede_STUDENTID_README.txt` – This file.

## REPOSITORY STRUCTURE

| Folder | Activity |
|---|---|
| `portfolio-1-database-design` | Database design and modelling |
| `portfolio-2-query-optimisation` | Query processing and optimisation |
| `portfolio-3-transactions-concurrency` | Transactions and concurrency |
| `portfolio-4-nosql` | NoSQL and advanced data models |
| `portfolio-5-distributed-cloud` | Distributed and cloud database exercise |

Each folder has its own README explaining what was done and how it was tested.

## HOW TO RUN

**MySQL (Portfolios 1 to 3):**

Use MySQL 8.0 and MySQL Workbench. Run `schema.sql`, followed by `seed_data.sql`, and then the scripts in the Portfolio 2 and Portfolio 3 folders.

**MongoDB (Portfolios 4 and 5):**

Use Python 3 and install the required packages:

```bash
pip install pymongo python-dotenv
```

Create a `.env` file containing `MONGODB_URI`. The connection string is not included in the repository for security reasons. Run `connect.py` and `import_bookings.py` inside the `portfolio-4-nosql` folder.

## DATA NOTE

All guest, staff and payment data used in this project are simulated. No real guest information is stored.

## PROGRESS

Work was committed progressively throughout the semester.

## AI USE DECLARATION

ChatGPT and Claude were used together as learning and development aids throughout the project. They assisted with understanding database concepts, planning and organising parts of the work, troubleshooting errors, reviewing SQL and Python scripts, and drafting and improving documentation.

I reviewed the suggestions from both tools and checked relevant technical information against my course materials, practical scripts and test outputs. I also ran the scripts and reviewed the results to confirm that the work reflected what I had actually implemented. The final work and decisions were reviewed by me.