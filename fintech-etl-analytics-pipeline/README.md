# Fintech ETL & Analytics Data Pipeline

## Overview

This project implements a reproducible ETL and analytics pipeline for synthetic fintech transaction data.

The pipeline extracts raw transaction records, cleans and transforms the data, validates data quality, produces a processed analytical dataset, and loads the cleaned data into PostgreSQL for SQL-based analytics.

The project demonstrates practical skills in data engineering, analytics engineering, SQL, Python, data quality, and financial data analysis.

## Business Objectives

- Build a reproducible ETL workflow
- Clean and normalize transaction data
- Detect and remove duplicate transactions
- Handle missing values
- Validate transaction data quality
- Create analytical features
- Load processed data into PostgreSQL
- Analyze transaction performance using SQL
- Identify trends by country, month, transaction type, and customer
- Translate analytical results into business insights

## Dataset

The dataset is fully synthetic and was generated specifically for this project.

The raw dataset contains 15,100 transaction records and includes intentionally introduced data-quality issues such as duplicate transactions, missing countries, inconsistent text formatting, and invalid transaction amounts.

After transformation and validation, the pipeline produces 14,950 clean transaction records.

### Dataset Fields

- `transaction_id`
- `customer_id`
- `transaction_date`
- `amount`
- `currency`
- `country`
- `transaction_type`
- `status`
- `transaction_month`
- `is_successful`

## ETL Pipeline

The pipeline follows four main stages:

### 1. Extract

Raw transaction data is loaded from:

`data/raw/transactions_raw.csv`

### 2. Transform

The transformation stage:

- Removes duplicate transaction IDs
- Handles missing countries
- Normalizes transaction type values
- Converts transaction dates to datetime
- Removes invalid transaction amounts
- Creates the transaction month
- Creates a successful transaction indicator

### 3. Validate

Automated data quality checks verify:

- Transaction ID uniqueness
- Positive transaction amounts
- Valid transaction dates
- Missing values
- Duplicate records

The pipeline stops if critical validation rules fail.

### 4. Load

The validated dataset is saved to:

`data/processed/transactions_clean.csv`

The processed dataset is also loaded into PostgreSQL for analytical queries.

## Pipeline Architecture

Raw CSV
→ Extract
→ Transform
→ Validate
→ Processed CSV
→ PostgreSQL
→ SQL Analytics
→ Business Insights

## Analytical Workflow

The project analyzes the processed transaction dataset using Python and PostgreSQL.

### Country Analysis

Transaction volume, transaction value, average transaction amount, and success rate are compared across countries.

### Monthly Analysis

Monthly transaction volume, total transaction value, and transaction success rates are analyzed to identify changes in activity over time.

### Transaction Type Analysis

Transaction performance is compared across:

- Card Payment
- Transfer
- Cash Withdrawal
- Online Payment

### Status Analysis

Transaction statuses are analyzed to understand the distribution of:

- Completed
- Pending
- Failed

### Customer Analysis

Customers are ranked according to transaction value to identify the highest-value transaction profiles.

### Data Quality Analysis

SQL validation queries verify:

- Total rows
- Unique transactions
- Duplicate records
- Invalid amounts
- Missing transaction dates

## Technologies

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- SQL
- PostgreSQL
- SQLAlchemy
- psycopg2

## Project Structure

    fintech-etl-analytics-pipeline/
    │
    ├── data/
    │   ├── raw/
    │   │   └── transactions_raw.csv
    │   │
    │   └── processed/
    │       └── transactions_clean.csv
    │
    ├── notebooks/
    │   └── etl_analytics.ipynb
    │
    ├── sql/
    │   └── analysis.sql
    │
    ├── src/
    │   └── etl_pipeline.py
    │
    ├── README.md
    └── requirements.txt

## Reproducibility

The raw dataset can be generated using:

    python src/etl_pipeline.py

The main analytical notebook is:

    notebooks/etl_analytics.ipynb

The SQL analysis is available in:

    sql/analysis.sql

## Results

The ETL pipeline successfully processed the synthetic transaction dataset.

Input:

- 15,100 raw records

Output:

- 14,950 validated records
- 10 analytical columns

The processed dataset passed the automated data quality validation checks.

## Business Applications

This type of pipeline can support fintech teams with:

- Transaction monitoring
- Financial reporting
- Operational analytics
- Payment performance analysis
- Customer segmentation
- Data quality monitoring
- Business intelligence
- Decision support

## Data Disclaimer

This project uses entirely synthetic data generated for portfolio and educational purposes.

It does not contain real customer information, real Revolut data, or confidential financial information.

## Portfolio Focus

Analytics Engineering | Data Engineering | Data Analytics | FinTech

## Author

Halimatou Diallo