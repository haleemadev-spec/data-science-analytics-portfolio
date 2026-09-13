-- Fintech Customer & Transaction Analytics
-- Business analysis queries

-- 1. Transaction volume and total value by customer segment
SELECT
    customer_segment,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_eur), 2) AS total_amount_eur,
    ROUND(AVG(amount_eur), 2) AS average_amount_eur
FROM transactions
GROUP BY customer_segment
ORDER BY total_amount_eur DESC;


-- 2. Transaction performance by country
SELECT
    country,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_eur), 2) AS total_amount_eur,
    ROUND(AVG(amount_eur), 2) AS average_amount_eur
FROM transactions
GROUP BY country
ORDER BY total_amount_eur DESC;


-- 3. Transaction performance by transaction type
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_eur), 2) AS total_amount_eur,
    ROUND(AVG(amount_eur), 2) AS average_amount_eur
FROM transactions
GROUP BY transaction_type
ORDER BY total_amount_eur DESC;


-- 4. Monthly transaction activity
SELECT
    DATE_TRUNC('month', transaction_date) AS month,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_eur), 2) AS total_amount_eur
FROM transactions
GROUP BY DATE_TRUNC('month', transaction_date)
ORDER BY month;


-- 5. Top 10 customers by transaction value
SELECT
    customer_id,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_eur), 2) AS total_amount_eur,
    ROUND(AVG(amount_eur), 2) AS average_amount_eur
FROM transactions
GROUP BY customer_id
ORDER BY total_amount_eur DESC
LIMIT 10;