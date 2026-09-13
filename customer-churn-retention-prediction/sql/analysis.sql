-- Customer Churn & Retention Prediction
-- SQL Analytics

-- 1. Overall churn rate
SELECT
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * AVG(churn), 2) AS churn_rate
FROM customers;


-- 2. Churn by country
SELECT
    country,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * AVG(churn), 2) AS churn_rate
FROM customers
GROUP BY country
ORDER BY churn_rate DESC;


-- 3. Churn by satisfaction score
SELECT
    satisfaction_score,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * AVG(churn), 2) AS churn_rate
FROM customers
GROUP BY satisfaction_score
ORDER BY satisfaction_score;


-- 4. Churn by premium status
SELECT
    premium_customer,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * AVG(churn), 2) AS churn_rate
FROM customers
GROUP BY premium_customer
ORDER BY premium_customer;


-- 5. Churn by activity level
SELECT
    CASE
        WHEN monthly_transactions < 10 THEN 'Low Activity'
        WHEN monthly_transactions < 25 THEN 'Medium Activity'
        ELSE 'High Activity'
    END AS activity_level,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * AVG(churn), 2) AS churn_rate
FROM customers
GROUP BY activity_level
ORDER BY churn_rate DESC;


-- 6. Churn by tenure
SELECT
    CASE
        WHEN tenure_months < 12 THEN 'Less than 1 year'
        WHEN tenure_months < 36 THEN '1 to 3 years'
        ELSE 'More than 3 years'
    END AS tenure_group,
    COUNT(*) AS customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * AVG(churn), 2) AS churn_rate
FROM customers
GROUP BY tenure_group
ORDER BY churn_rate DESC;


-- 7. High-risk customer profile
SELECT
    customer_id,
    country,
    tenure_months,
    monthly_transactions,
    app_sessions_monthly,
    satisfaction_score,
    support_contacts,
    failed_transactions,
    churn
FROM customers
WHERE churn = 1
ORDER BY satisfaction_score ASC, monthly_transactions ASC
LIMIT 20;