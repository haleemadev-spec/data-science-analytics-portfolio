# Customer Churn & Retention Prediction

## Overview

This project develops a machine learning solution to identify fintech customers at risk of churn and support customer retention strategies.

The project combines exploratory data analysis, statistical analysis, feature engineering, supervised machine learning, model evaluation, and business interpretation.

## Business Problem

Customer churn can negatively affect revenue, engagement, and long-term customer value.

The objective of this project is to identify behavioral and customer-level factors associated with churn and build a predictive model that can help prioritize retention efforts.

## Dataset

The dataset contains 5,000 synthetic fintech customers.

The dataset includes:

- Age
- Country
- Tenure
- Monthly transaction activity
- Average transaction amount
- Monthly application sessions
- Customer support contacts
- Card usage
- Satisfaction score
- Premium customer status
- International transaction activity
- Failed transactions
- Churn indicator

The data is entirely synthetic and was generated specifically for this portfolio project.

## Analytical Objectives

- Measure the overall churn rate
- Analyze customer characteristics associated with churn
- Identify behavioral patterns linked to customer retention
- Engineer features for machine learning
- Train classification models
- Compare Logistic Regression and Random Forest
- Evaluate model performance
- Identify important churn-related features
- Produce customer-level churn risk predictions
- Translate model results into retention recommendations

## Machine Learning Workflow

### 1. Data Preparation

The dataset is loaded and checked for missing values and basic quality issues.

### 2. Exploratory Data Analysis

The analysis examines:

- Churn distribution
- Satisfaction and churn
- Customer activity and churn
- Customer engagement
- Support interactions
- Tenure

### 3. Feature Engineering

Numerical variables are standardized and the country variable is one-hot encoded.

### 4. Model Training

Two classification models are trained:

- Logistic Regression
- Random Forest

### 5. Model Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

### 6. Feature Importance

Random Forest feature importance is used to identify the variables that contribute most to churn prediction.

### 7. Customer Risk Scoring

The model produces customer-level churn probabilities that can be used to prioritize retention actions.

## Business Interpretation

The analysis is designed to help identify customers showing behavioral signals associated with churn.

Potential retention actions include:

- Re-engagement campaigns for low-activity customers
- Personalized offers for customers with declining engagement
- Improved support for customers with repeated support contacts
- Targeted interventions for customers with low satisfaction
- Monitoring customers with high predicted churn probability

These recommendations are analytical suggestions based on synthetic data and should be validated using real customer experiments.

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

    customer-churn-retention-prediction/
    │
    ├── data/
    │   ├── customers.csv
    │   └── churn_predictions.csv
    │
    ├── notebooks/
    │   └── churn_prediction_analysis.ipynb
    │
    ├── sql/
    │   └── analysis.sql
    │
    ├── src/
    │   └── data_generation.py
    │
    ├── README.md
    └── requirements.txt

## Reproducibility

Generate the synthetic customer dataset with:

    python src/data_generation.py

Run the main analysis notebook:

    notebooks/churn_prediction_analysis.ipynb

## Data Disclaimer

This project uses entirely synthetic data generated for portfolio and educational purposes.

It does not contain real customer information, real Revolut data, or confidential financial information.

## Portfolio Focus

Data Science | Machine Learning | Customer Analytics | FinTech

## Author

Halimatou Diallo