-- ============================================================
-- BLUESTOCK MF — 10 ANALYTICAL SQL QUERIES
-- ============================================================

-- Q1: Top 5 Fund Houses by Latest AUM
SELECT fund_house,
       ROUND(MAX(aum_lakh_crore), 2) AS latest_aum_lakh_crore
FROM fact_aum
WHERE date = (SELECT MAX(date) FROM fact_aum)
ORDER BY latest_aum_lakh_crore DESC
LIMIT 5;

-- Q2: Average Monthly NAV per Fund (last 12 months)
SELECT f.scheme_name,
       STRFTIME('%Y-%m', n.date)     AS month,
       ROUND(AVG(n.nav), 4)          AS avg_nav
FROM fact_nav n
JOIN dim_fund f ON n.amfi_code = f.amfi_code
WHERE n.date >= DATE('now', '-12 months')
GROUP BY f.scheme_name, month
ORDER BY f.scheme_name, month;

-- Q3: SIP YoY Growth (from fact_transactions)
SELECT STRFTIME('%Y', transaction_date) AS year,
       COUNT(*)                          AS sip_count,
       ROUND(SUM(amount_inr)/1e7, 2)    AS total_sip_crore
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- Q4: Transaction Count and Volume by State
SELECT state,
       COUNT(*)                          AS txn_count,
       ROUND(SUM(amount_inr)/1e7, 2)    AS total_amount_crore
FROM fact_transactions
GROUP BY state
ORDER BY total_amount_crore DESC;

-- Q5: Funds with Expense Ratio < 1%
SELECT f.scheme_name,
       f.fund_house,
       f.sub_category,
       f.plan,
       f.expense_ratio_pct
FROM dim_fund f
WHERE f.expense_ratio_pct < 1.0
ORDER BY f.expense_ratio_pct ASC;

-- Q6: Top 5 Funds by 5-Year Return
SELECT scheme_name,
       fund_house,
       plan,
       return_5yr_pct,
       sharpe_ratio,
       morningstar_rating
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Q7: Fund Count by Category and Risk Grade
SELECT f.category,
       f.risk_category,
       COUNT(*) AS scheme_count
FROM dim_fund f
GROUP BY f.category, f.risk_category
ORDER BY scheme_count DESC;

-- Q8: KYC Status Summary
SELECT kyc_status,
       COUNT(*)                       AS investor_count,
       ROUND(COUNT(*) * 100.0 /
         (SELECT COUNT(*) FROM fact_transactions), 2) AS pct
FROM fact_transactions
GROUP BY kyc_status
ORDER BY investor_count DESC;

-- Q9: Monthly Redemption vs SIP Volume
SELECT STRFTIME('%Y-%m', transaction_date) AS month,
       ROUND(SUM(CASE WHEN transaction_type='SIP'
                      THEN amount_inr ELSE 0 END)/1e7, 2) AS sip_crore,
       ROUND(SUM(CASE WHEN transaction_type='Redemption'
                      THEN amount_inr ELSE 0 END)/1e7, 2) AS redemption_crore
FROM fact_transactions
GROUP BY month
ORDER BY month;

-- Q10: Best Alpha Funds (Direct Plans only)
SELECT p.scheme_name,
       p.fund_house,
       p.alpha,
       p.beta,
       p.sharpe_ratio,
       p.return_3yr_pct,
       p.expense_ratio_pct
FROM fact_performance p
WHERE p.plan = 'Direct'
ORDER BY p.alpha DESC
LIMIT 10;