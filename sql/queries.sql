-- =====================================================
-- Financial Fraud Detection & Risk Analytics System
-- SQL Business Analysis Queries
-- =====================================================


-- =====================================================
-- Query 1: Total Fraud vs Normal Transactions
-- =====================================================

SELECT 
    Class,
    COUNT(*) AS total_transactions
FROM creditcard
GROUP BY Class
ORDER BY Class;


-- =====================================================
-- Query 2: Fraud Percentage Calculation
-- =====================================================

SELECT 
    ROUND(
        (SUM(CASE WHEN Class = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*),
        4
    ) AS fraud_percentage
FROM creditcard;


-- =====================================================
-- Query 3: Average Fraud Transaction Amount
-- =====================================================

SELECT 
    ROUND(AVG(Amount), 2) AS avg_fraud_amount
FROM creditcard
WHERE Class = 1;


-- =====================================================
-- Query 4: Top High-Value Fraud Transactions
-- =====================================================

SELECT 
    Time,
    Amount,
    Class
FROM creditcard
WHERE Class = 1
ORDER BY Amount DESC
LIMIT 10;


-- =====================================================
-- Query 5: Top 10 Highest Transactions Overall
-- =====================================================

SELECT 
    Time,
    Amount,
    Class
FROM creditcard
ORDER BY Amount DESC
LIMIT 10;


-- =====================================================
-- Query 6: Fraud Transactions Greater Than Average Fraud Amount
-- =====================================================

SELECT 
    COUNT(*) AS fraud_above_average
FROM creditcard
WHERE Class = 1
AND Amount > (
    SELECT AVG(Amount)
    FROM creditcard
    WHERE Class = 1
);


-- =====================================================
-- Query 7: Average Transaction Amount by Class
-- =====================================================

SELECT 
    Class,
    ROUND(AVG(Amount), 2) AS avg_transaction_amount
FROM creditcard
GROUP BY Class
ORDER BY Class;


-- =====================================================
-- Query 8: Minimum, Maximum, and Average Fraud Amount
-- =====================================================

SELECT 
    MIN(Amount) AS min_fraud_amount,
    MAX(Amount) AS max_fraud_amount,
    ROUND(AVG(Amount), 2) AS avg_fraud_amount
FROM creditcard
WHERE Class = 1;


-- =====================================================
-- Query 9: Total Fraud Amount (Potential Financial Loss)
-- =====================================================

SELECT 
    ROUND(SUM(Amount), 2) AS total_fraud_amount
FROM creditcard
WHERE Class = 1;


-- =====================================================
-- Query 10: Fraud Transactions by Time Range
-- =====================================================

SELECT 
    CASE
        WHEN Time < 43200 THEN '0-12 Hours'
        WHEN Time < 86400 THEN '12-24 Hours'
        WHEN Time < 129600 THEN '24-36 Hours'
        ELSE '36-48 Hours'
    END AS time_range,
    COUNT(*) AS fraud_count
FROM creditcard
WHERE Class = 1
GROUP BY time_range
ORDER BY fraud_count DESC;


-- =====================================================
-- Query 11: Count of Zero Amount Transactions
-- =====================================================

SELECT 
    COUNT(*) AS zero_amount_transactions
FROM creditcard
WHERE Amount = 0;


-- =====================================================
-- Query 12: Fraud Transactions with Zero Amount
-- =====================================================

SELECT 
    COUNT(*) AS zero_amount_fraud_transactions
FROM creditcard
WHERE Class = 1
AND Amount = 0;


-- =====================================================
-- Query 13: Percentage of Fraud in Top 100 Highest Transactions
-- =====================================================

SELECT 
    ROUND(
        (SUM(Class) * 100.0) / COUNT(*),
        2
    ) AS fraud_percentage_top_100
FROM (
    SELECT *
    FROM creditcard
    ORDER BY Amount DESC
    LIMIT 100
);


-- =====================================================
-- Query 14: Fraud Count by Amount Category
-- =====================================================

SELECT 
    CASE
        WHEN Amount < 50 THEN 'Low Value'
        WHEN Amount < 200 THEN 'Medium Value'
        ELSE 'High Value'
    END AS amount_category,
    COUNT(*) AS fraud_count
FROM creditcard
WHERE Class = 1
GROUP BY amount_category
ORDER BY fraud_count DESC;


-- =====================================================
-- Query 15: Final Executive KPI Summary
-- =====================================================

SELECT
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN Class = 1 THEN 1 ELSE 0 END) AS total_fraud_transactions,
    ROUND(
        (SUM(CASE WHEN Class = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*),
        4
    ) AS fraud_percentage,
    ROUND(AVG(CASE WHEN Class = 1 THEN Amount END), 2) AS avg_fraud_amount,
    ROUND(SUM(CASE WHEN Class = 1 THEN Amount END), 2) AS total_fraud_loss
FROM creditcard;