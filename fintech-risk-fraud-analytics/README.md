# Fintech Risk & Fraud Analytics

## Overview

This project develops a financial risk and fraud analytics solution using synthetic fintech transaction data.

The project combines exploratory data analysis, feature engineering, machine learning, fraud probability estimation, risk scoring, PostgreSQL, and SQL analytics.

## Business Problem

Financial platforms must identify suspicious transactions while minimizing unnecessary friction for legitimate customers.

The objective of this project is to identify transaction patterns associated with fraud, build classification models, estimate fraud probabilities, and produce risk scores that can support transaction monitoring and investigation workflows.

## Dataset

The dataset contains 15,000 synthetic fintech transactions.

The dataset includes:

- Transaction amount
- Country
- Transaction type
- Device
- Transaction hour
- Customer transaction frequency
- Customer average transaction amount
- International transaction indicator
- Failed transaction count
- Fraud indicator

The data is entirely synthetic and was generated specifically for this portfolio project.

## Analytical Objectives

- Measure the overall fraud rate
- Analyze fraud patterns by country
- Analyze fraud by transaction type
- Analyze fraud by transaction hour
- Identify high-value transaction anomalies
- Engineer fraud-related features
- Train classification models
- Compare Logistic Regression and Random Forest
- Evaluate fraud detection performance
- Estimate transaction fraud probability
- Produce transaction-level risk scores
- Categorize transactions into risk levels
- Translate analytical findings into business recommendations

## Feature Engineering

The project creates analytical features including:

- Amount deviation from customer average
- Transaction amount ratio
- High amount indicator
- Night transaction indicator
- Failed transaction ratio

These features help capture behavioral patterns that may be associated with suspicious activity.

## Machine Learning

Two supervised learning models are evaluated:

- Logistic Regression
- Random Forest

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

Recall is particularly important in fraud detection because failing to identify fraudulent transactions can create significant financial and operational risk.

## Risk Scoring

The Random Forest model produces a fraud probability for each transaction.

The probability is converted into a risk score from 0 to 100.

Transactions are categorized as:

- Low Risk
- Medium Risk
- High Risk

The highest-risk transactions can be prioritized for additional investigation.

## Business Applications

This type of fraud analytics solution can support:

- Transaction monitoring
- Fraud investigation
- Risk-based transaction review
- Suspicious activity detection
- Payment security
- Customer protection
- Financial risk management

Potential operational actions include:

- Reviewing high-risk transactions
- Applying additional verification to suspicious activity
- Monitoring unusual transaction behavior
- Investigating abnormal transaction amounts
- Improving fraud detection rules using model insights

These recommendations are based on synthetic data and should be validated with real transaction data before operational deployment.

## SQL Analytics

PostgreSQL queries analyze:

- Overall fraud rate
- Fraud by country
- Fraud by transaction type
- Fraud by transaction hour
- International transaction risk
- Fraudulent transaction amounts
- Data quality

## Technologies

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- PostgreSQL
- SQL
- SQLAlchemy
- psycopg2

## Project Structure

    fintech-risk-fraud-analytics/
    ¦
    +-- data/
    ¦   +-- transactions.csv
    ¦   +-- fraud_risk_scores.csv
    ¦
    +-- notebooks/
    ¦   +-- risk_fraud_analysis.ipynb
    ¦
    +-- sql/
    ¦   +-- analysis.sql
    ¦
    +-- src/
    ¦   +-- data_generation.py
    ¦
    +-- README.md
    +-- requirements.txt

## Reproducibility

Generate the synthetic transaction dataset with:

    python src/data_generation.py

Run the analytical notebook:

    notebooks/risk_fraud_analysis.ipynb

Run the SQL analytics against the PostgreSQL database:

    sql/analysis.sql

## Data Disclaimer

This project uses entirely synthetic data generated for portfolio and educational purposes.

It does not contain real customer information, real Revolut data, or confidential financial information.

## Portfolio Focus

Risk Analytics | Fraud Detection | Machine Learning | FinTech

## Author

Halimatou Diallo
