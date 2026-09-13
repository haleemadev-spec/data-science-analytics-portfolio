-- Product Analytics & Conversion Funnel

-- 1. Activation rate by acquisition channel

SELECT
    acquisition_channel,
    COUNT(*) AS users,
    SUM(active) AS active_users,
    ROUND(
        SUM(active)::numeric / COUNT(*) * 100,
        2
    ) AS activation_rate
FROM funnel_users
GROUP BY acquisition_channel
ORDER BY activation_rate DESC;


-- 2. Activation rate by country

SELECT
    country,
    COUNT(*) AS users,
    SUM(active) AS active_users,
    ROUND(
        SUM(active)::numeric / COUNT(*) * 100,
        2
    ) AS activation_rate
FROM funnel_users
GROUP BY country
ORDER BY activation_rate DESC;


-- 3. Monthly activation

SELECT
    DATE_TRUNC('month', event_date) AS month,
    COUNT(*) AS users,
    SUM(active) AS active_users,
    ROUND(
        SUM(active)::numeric / COUNT(*) * 100,
        2
    ) AS activation_rate
FROM funnel_users
GROUP BY month
ORDER BY month;


-- 4. Funnel performance

SELECT
    COUNT(*) AS visited_users,
    SUM(signed_up) AS signed_up_users,
    SUM(verified) AS verified_users,
    SUM(funded) AS funded_users,
    SUM(active) AS active_users
FROM funnel_users;