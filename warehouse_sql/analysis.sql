-- Total revenue
SELECT SUM(revenue) AS total_revenue
FROM transactions_clean;

-- Revenue by product
SELECT product, SUM(revenue) AS total_revenue
FROM transactions_clean
GROUP BY product
ORDER BY total_revenue DESC;

-- Revenue by region
SELECT region, SUM(revenue) AS total_revenue
FROM transactions_clean
GROUP BY region
ORDER BY total_revenue DESC;

-- Daily revenue trend
SELECT date, SUM(revenue) AS daily_revenue
FROM transactions_clean
GROUP BY date
ORDER BY date;

-- Top 10 highest transactions
SELECT *
FROM transactions_clean
ORDER BY revenue DESC
LIMIT 10;
