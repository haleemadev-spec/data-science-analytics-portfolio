-- Fintech Risk & Fraud Analytics

-- 1. Overall fraud rate
SELECT
    COUNT(*) AS transactions,
    SUM(fraud) AS fraudulent_transactions,
    ROUND(100.0 * AVG(fraud), 2) AS fraud_rate
FROM transactions;

-- 2. Fraud by country
SELECT
    country,
    COUNT(*) AS transactions,
    SUM(fraud) AS fraudulent_transactions,
    ROUND(100.0 * AVG(fraud), 2) AS fraud_rate
FROM transactions
GROUP BY country
ORDER BY fraud_rate DESC;

-- 3. Fraud by transaction type
SELECT
    transaction_type,
    COUNT(*) AS transactions,
    SUM(fraud) AS fraudulent_transactions,
    ROUND(100.0 * AVG(fraud), 2) AS fraud_rate
FROM transactions
GROUP BY transaction_type
ORDER BY fraud_rate DESC;

-- 4. Fraud by transaction hour
SELECT
    transaction_hour,
    COUNT(*) AS transactions,
    SUM(fraud) AS fraudulent_transactions,
    ROUND(100.0 * AVG(fraud), 2) AS fraud_rate
FROM transactions
GROUP BY transaction_hour
ORDER BY transaction_hour;

-- 5. Fraud by international activity
SELECT
    international_transaction,
    COUNT(*) AS transactions,
    SUM(fraud) AS fraudulent_transactions,
    ROUND(100.0 * AVG(fraud), 2) AS fraud_rate
FROM transactions
GROUP BY international_transaction;

-- 6. Fraudulent transaction amounts
SELECT
    fraud,
    COUNT(*) AS transactions,
    ROUND(AVG(transaction_amount), 2) AS average_amount,
    ROUND(MAX(transaction_amount), 2) AS maximum_amount
FROM transactions
GROUP BY fraud;

-- 7. Data quality
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT transaction_id) AS unique_transactions,
    COUNT(*) - COUNT(DISTINCT transaction_id) AS duplicate_rows,
    COUNT(*) FILTER (WHERE transaction_amount <= 0) AS invalid_amounts
FROM transactions;
