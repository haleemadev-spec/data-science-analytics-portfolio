-- Fintech ETL & Analytics Data Pipeline
-- SQL Analytics

-- 1. Overall transaction performance
SELECT
    COUNT(*) AS transactions,
    COUNT(DISTINCT customer_id) AS customers,
    SUM(amount) AS total_amount,
    ROUND(AVG(amount), 2) AS average_amount,
    ROUND(100.0 * AVG(is_successful), 2) AS success_rate
FROM transactions_clean;


-- 2. Performance by country
SELECT
    country,
    COUNT(*) AS transactions,
    SUM(amount) AS total_amount,
    ROUND(AVG(amount), 2) AS average_amount,
    ROUND(100.0 * AVG(is_successful), 2) AS success_rate
FROM transactions_clean
GROUP BY country
ORDER BY total_amount DESC;


-- 3. Monthly transaction performance
SELECT
    transaction_month,
    COUNT(*) AS transactions,
    SUM(amount) AS total_amount,
    ROUND(100.0 * AVG(is_successful), 2) AS success_rate
FROM transactions_clean
GROUP BY transaction_month
ORDER BY transaction_month;


-- 4. Performance by transaction type
SELECT
    transaction_type,
    COUNT(*) AS transactions,
    SUM(amount) AS total_amount,
    ROUND(AVG(amount), 2) AS average_amount,
    ROUND(100.0 * AVG(is_successful), 2) AS success_rate
FROM transactions_clean
GROUP BY transaction_type
ORDER BY total_amount DESC;


-- 5. Performance by transaction status
SELECT
    status,
    COUNT(*) AS transactions,
    SUM(amount) AS total_amount,
    ROUND(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),
        2
    ) AS transaction_share
FROM transactions_clean
GROUP BY status
ORDER BY transactions DESC;


-- 6. Top customers by transaction value
SELECT
    customer_id,
    COUNT(*) AS transactions,
    SUM(amount) AS total_amount,
    ROUND(AVG(amount), 2) AS average_amount
FROM transactions_clean
GROUP BY customer_id
ORDER BY total_amount DESC
LIMIT 10;


-- 7. Data quality validation
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT transaction_id) AS unique_transactions,
    COUNT(*) - COUNT(DISTINCT transaction_id) AS duplicate_rows,
    COUNT(*) FILTER (WHERE amount <= 0) AS invalid_amounts,
    COUNT(*) FILTER (WHERE transaction_date IS NULL) AS missing_dates
FROM transactions_clean;