# Fintech Customer & Transaction Analytics

**Author:** Halimatou Diallo

## Overview

This project analyzes synthetic financial transaction data to identify customer behavior, transaction patterns, geographic trends, and high-value activity.

The project demonstrates an end-to-end financial data analytics workflow using Python, SQL, Pandas, statistical analysis, data visualization, and PostgreSQL.

## Business Objectives

- Analyze transaction behavior across customer segments
- Compare transaction activity across countries
- Identify the most significant transaction types
- Analyze monthly transaction trends
- Identify high-value customers
- Detect unusual transaction values through statistical analysis
- Translate analytical results into actionable business insights

## Dataset

The dataset is fully synthetic and was generated specifically for this project.

It contains 15,000 transactions from 1,000 customers covering the year 2025.

The dataset contains the following fields:

- transaction_id
- customer_id
- transaction_date
- transaction_type
- merchant_category
- amount_eur
- country
- customer_segment

Countries represented:

- Senegal
- France
- United Kingdom
- Germany
- Spain
- Portugal

Customer segments:

- Standard
- Premium
- Business

Transaction types:

- Card Payment
- Transfer
- Cash Withdrawal
- Online Payment

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

    fintech-customer-transaction-analytics/
    │
    ├── data/
    │   └── transactions.csv
    │
    ├── notebooks/
    │   └── customer_transaction_analysis.ipynb
    │
    ├── sql/
    │   └── analysis.sql
    │
    ├── src/
    │   └── data_generation.py
    │
    ├── README.md
    └── requirements.txt

## Analytical Workflow

### 1. Data Generation

A reproducible synthetic transaction dataset was generated using Python.

The generation process uses a fixed random seed to ensure reproducibility.

### 2. Data Quality Analysis

The dataset was checked for:

- Missing values
- Duplicate records
- Negative transaction amounts
- Data types
- Unique values
- Structural consistency

The dataset contains 15,000 transaction records with no missing values, no duplicate records, and no negative transaction amounts.

### 3. Exploratory Data Analysis

Descriptive statistics were calculated to understand:

- Transaction volume
- Average transaction amount
- Median transaction amount
- Distribution of transaction values
- Statistical skewness
- High-value transactions

The transaction amount distribution is strongly right-skewed, with a skewness value of approximately 8.90.

### 4. Customer Segment Analysis

Transaction activity was compared across Standard, Premium, and Business customers using:

- Transaction count
- Total transaction value
- Average transaction value
- Median transaction value

The analysis shows that Standard customers generate the highest transaction volume, while Premium and Business customers generate substantially higher average transaction values.

### 5. Geographic Analysis

Transaction activity was analyzed by country using:

- Transaction volume
- Total transaction value
- Average transaction value

Senegal represents the largest transaction volume and total transaction value in the synthetic dataset.

### 6. Transaction Type Analysis

The following transaction types were compared:

- Card Payment
- Transfer
- Online Payment
- Cash Withdrawal

The analysis covers:

- Transaction volume
- Total transaction value
- Average transaction value

Card payments represent the largest transaction category by total transaction value.

### 7. Temporal Analysis

Monthly transaction trends were analyzed using:

- Transaction volume
- Total transaction value
- Average transaction value

The analysis helps identify changes in transaction activity throughout the year.

### 8. Statistical Analysis

Transaction amount distribution was examined using descriptive statistics and skewness.

The strong right-skew indicates that a relatively small number of unusually large transactions have a significant impact on the overall distribution.

### 9. Data Visualization

The project includes visualizations covering:

- Monthly transaction volume
- Total transaction value by customer segment
- Total transaction value by transaction type

These visualizations support the interpretation of customer behavior and transaction patterns.

### 10. SQL Analysis

The transaction dataset was loaded into PostgreSQL and analyzed using SQL queries covering:

- Customer segment performance
- Country-level activity
- Transaction type performance
- Monthly transaction trends
- Top customers by transaction value

The PostgreSQL database contains the complete set of 15,000 transactions.

## Key Findings

- Standard customers generate the highest transaction volume.
- Premium customers have a significantly higher average transaction value than Standard customers.
- Business customers have the highest average transaction value.
- Card payments represent the largest transaction category by total transaction value.
- Senegal represents the largest transaction volume and total transaction value among the countries in the synthetic dataset.
- Transaction activity varies throughout the year.
- Transaction amounts are strongly right-skewed.
- A small number of high-value transactions have a significant impact on the distribution.
- High-value customers can be identified through aggregated transaction behavior.

## Business Interpretation

The analysis demonstrates how financial transaction data can support business and product decisions.

Potential applications include:

- Customer segmentation
- Product performance analysis
- High-value customer identification
- Transaction monitoring
- Financial reporting
- Customer behavior analysis
- Risk and anomaly investigation
- Data-driven product decision-making

## Reproducibility

The synthetic dataset can be regenerated using:

    python src/data_generation.py

The main analytical notebook is available at:

    notebooks/customer_transaction_analysis.ipynb

The SQL analysis is available at:

    sql/analysis.sql

## Data Disclaimer

This project uses entirely synthetic data generated for portfolio and educational purposes.

It does not contain real customer information, real Revolut data, or confidential financial information.

The project is intended to demonstrate practical skills in financial data analytics, SQL, Python, statistical analysis, data visualization, and PostgreSQL.

## Portfolio Focus

Data Science & Analytics | FinTech