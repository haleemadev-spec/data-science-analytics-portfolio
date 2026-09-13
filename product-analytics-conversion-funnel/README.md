# Product Analytics & Conversion Funnel

## Overview

This project analyzes a synthetic fintech user journey to understand conversion, activation, acquisition performance, and user drop-off across the product funnel.

The analysis follows a typical fintech conversion funnel:

**Visited → Signed Up → Verified → Funded → Active**

The project combines Python, SQL, PostgreSQL, statistical analysis, data visualization, cohort analysis, and A/B testing simulation to demonstrate practical product analytics skills.

## Business Objectives

- Measure conversion rates across the user funnel
- Identify the largest drop-off points
- Compare activation performance across acquisition channels
- Compare activation performance across countries
- Analyze monthly activation trends
- Perform cohort-based activation analysis
- Simulate an A/B experiment
- Translate analytical results into product recommendations

## Dataset

The dataset is fully synthetic and was generated specifically for this project.

It contains 5,000 synthetic users distributed across six countries and five acquisition channels.

Each user contains information about their progression through the product funnel.

### Dataset Fields

- `user_id`
- `event_date`
- `country`
- `acquisition_channel`
- `visited`
- `signed_up`
- `verified`
- `funded`
- `active`

### Countries

- Senegal
- France
- United Kingdom
- Germany
- Spain
- Portugal

### Acquisition Channels

- Organic
- Paid Search
- Social Media
- Referral
- Email

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

    product-analytics-conversion-funnel/
    │
    ├── data/
    │   └── funnel_users.csv
    │
    ├── notebooks/
    │   └── product_funnel_analysis.ipynb
    │
    ├── sql/
    │   └── analysis.sql
    │
    ├── src/
    │   ├── data_generation.py
    │   └── funnel_data_generation.py
    │
    ├── README.md
    └── requirements.txt

## Analytical Workflow

### 1. Data Generation

A reproducible synthetic dataset of 5,000 users was generated using Python with a fixed random seed.

### 2. Funnel Analysis

The user journey was analyzed across five stages:

1. Visited
2. Signed Up
3. Verified
4. Funded
5. Active

For each stage, the analysis measures user volume, cumulative conversion, and drop-off.

### 3. Acquisition Channel Analysis

Activation performance was compared across:

- Organic
- Paid Search
- Social Media
- Referral
- Email

The analysis identifies acquisition channels associated with stronger downstream activation.

### 4. Geographic Analysis

Activation rates were compared across the six countries represented in the synthetic dataset.

This provides a geographic view of product engagement and user activation.

### 5. Cohort Analysis

Users were grouped by event month to compare monthly activation performance.

The cohort analysis helps identify changes in activation performance over time.

### 6. A/B Test Simulation

A simulated A/B experiment was performed by randomly assigning users to two variants and comparing activation rates.

Because the dataset is synthetic and the experiment is simulated, the results are presented as an analytical demonstration rather than causal evidence of product impact.

### 7. SQL Analysis

The dataset is analyzed using PostgreSQL queries covering:

- Activation by acquisition channel
- Activation by country
- Monthly activation
- Funnel performance

## Key Product Questions

The analysis is designed to answer questions such as:

- Where do users drop out of the funnel?
- Which acquisition channels generate stronger activation?
- Which countries show the highest activation rates?
- How does activation vary over time?
- What differences appear between experimental variants?
- Which part of the user journey should product teams prioritize?

## Business Interpretation

Conversion funnel analysis can help product teams identify where users are lost during onboarding and activation.

The analysis can support decisions related to:

- Onboarding optimization
- Verification experience
- Funding conversion
- Acquisition strategy
- Product experimentation
- Customer activation
- Growth performance

## Reproducibility

The synthetic dataset can be regenerated with:

    python src/funnel_data_generation.py

The main analysis notebook is:

    notebooks/product_funnel_analysis.ipynb

The SQL analysis is:

    sql/analysis.sql

## Data Disclaimer

This project uses entirely synthetic data generated for portfolio and educational purposes.

It does not contain real customer information, real Revolut data, or confidential financial information.

## Portfolio Focus

Product Analytics | Data Science | FinTech

## Author

Halimatou Diallo