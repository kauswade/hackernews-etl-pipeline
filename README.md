# Automated Tech Trend Analysis Pipeline

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Mage.ai](https://img.shields.io/badge/Orchestration-Mage.ai-purple)
![Postgres](https://img.shields.io/badge/Data_Warehouse-PostgreSQL-blue)

## Project Overview
This project is an end-to-end Data Engineering ETL Pipeline designed to identify emerging technology trends by analyzing daily stories from HackerNews.

It is fully containerized using Docker and orchestrated with Mage.ai, ensuring that data extraction, transformation, and loading (ETL) occur automatically on a daily schedule.

### Key Features
* **Orchestration:** Automated daily pipeline using Mage.ai (Batch Processing).
* **Ingestion:** Fetches top 100 stories via the HackerNews API.
* **Transformation:** Uses Pandas for text processing, tokenization, and keyword frequency analysis.
* **Warehousing:** Loads structured data into a PostgreSQL data warehouse.
* **Infrastructure:** Defined as code (IaC) using docker-compose.

---

## Architecture

**Flow:** API (Source) -> Docker Container (Mage) -> Transformation Logic -> Docker Container (Postgres)

1. **Extract:** Pull raw JSON data from the API.
2. **Transform:**
    * Clean special characters.
    * Explode titles into individual words.
    * Filter stop words (common English words).
    * Aggregate counts per keyword.
3. **Load:** Append results to the "tech_trends_daily" table in Postgres.

![Pipeline Flow](assets\pipeline_flow.png)

---

## Technologies Used
* **Orchestrator:** Mage.ai
* **Containerization:** Docker & Docker Compose
* **Database:** PostgreSQL (v14)
* **Language:** Python 3 (Pandas, SQLAlchemy)

---

## Setup & Installation

**Prerequisites:**
* Docker Desktop installed and running.
* Git.

**Step 1: Clone the Repository**
```bash
git clone [https://github.com/kauswade/hackernews-etl-pipeline.git](https://github.com/kauswade/hackernews-etl-pipeline.git)
cd hackernews-etl-pipeline
```

**Step 2: Configure Environment**
Create a .env file in the root directory (this file is excluded from version control for security):

```text
POSTGRES_DB=dev
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

**Step 3: Launch the Infrastructure**
```bash
docker compose up
```
* The Mage UI will be available at: http://localhost:6789
* Postgres will be running on port: 5432

## Data Schema

The final output in PostgreSQL ("tech_trends_daily" table) contains the following schema:

| Column | Type | Description |
| :--- | :--- | :--- |
| keyword | String | The tech term (e.g., "rust", "ai") |
| count | Integer | Frequency of the keyword in top stories |
| date | Date | Date of data capture |

---

## How to Run the Pipeline

1. Open the Mage UI at http://localhost:6789.
2. Navigate to the "hackernews_daily" pipeline.
3. Click "Run @once" to trigger a manual run.
4. Check the "Triggers" tab to verify the active daily schedule (configured to run daily at 08:00 UTC).