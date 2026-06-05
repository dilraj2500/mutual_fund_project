# Bluestock Mutual Fund — Data Dictionary

## 1. dim_fund (Fund Master)
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Unique AMFI scheme code (Primary Key) |
| fund_house | TEXT | AMC name (e.g. SBI Mutual Fund) |
| scheme_name | TEXT | Full scheme name |
| category | TEXT | Equity / Debt / Hybrid |
| sub_category | TEXT | Large Cap / Mid Cap / Small Cap etc. |
| plan | TEXT | Regular or Direct |
| launch_date | DATE | Scheme launch date |
| benchmark | TEXT | Benchmark index name |
| expense_ratio_pct | REAL | Annual expense ratio in % |
| exit_load_pct | REAL | Exit load percentage |
| min_sip_amount | REAL | Minimum SIP amount in ₹ |
| min_lumpsum_amount | REAL | Minimum lumpsum in ₹ |
| fund_manager | TEXT | Name of fund manager |
| risk_category | TEXT | Low / Moderate / High / Very High |
| sebi_category_code | TEXT | SEBI internal category code |

## 2. dim_date (Date Dimension)
| Column | Type | Description |
|--------|------|-------------|
| date | DATE | Calendar date (Primary Key) |
| year | INTEGER | Calendar year |
| month | INTEGER | Month number (1–12) |
| month_name | TEXT | Month name (January etc.) |
| quarter | INTEGER | Quarter (1–4) |
| day_of_week | TEXT | Monday to Friday |
| is_month_end | INTEGER | 1 if last trading day of month |

## 3. fact_nav (NAV History)
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | FK → dim_fund |
| date | DATE | NAV date (trading days only) |
| nav | REAL | Net Asset Value in ₹ |

## 4. fact_transactions (Investor Transactions)
| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | FK → dim_fund |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount in ₹ |
| state | TEXT | Indian state of investor |
| city | TEXT | City of investor |
| city_tier | TEXT | T30 (top 30 cities) or B30 |
| age_group | TEXT | 18-25 / 26-35 / 36-45 / 46-55 / 56+ |
| gender | TEXT | Male / Female |
| annual_income_lakh | REAL | Annual income in ₹ Lakh |
| payment_mode | TEXT | UPI / Mandate / Cheque / Net Banking |
| kyc_status | TEXT | Verified / Pending / Rejected |

## 5. fact_performance (Scheme Performance)
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | FK → dim_fund (Primary Key) |
| return_1yr_pct | REAL | 1-year absolute return % |
| return_3yr_pct | REAL | 3-year CAGR % |
| return_5yr_pct | REAL | 5-year CAGR % |
| benchmark_3yr_pct | REAL | Benchmark 3yr return % |
| alpha | REAL | Jensen's Alpha (annualised) |
| beta | REAL | Beta vs benchmark |
| sharpe_ratio | REAL | Sharpe ratio (Rf = 6.5%) |
| sortino_ratio | REAL | Sortino ratio |
| std_dev_ann_pct | REAL | Annualised standard deviation % |
| max_drawdown_pct | REAL | Maximum drawdown % |
| aum_crore | REAL | AUM in ₹ Crore |
| expense_ratio_pct | REAL | TER in % |
| morningstar_rating | INTEGER | 1–5 star rating |
| risk_grade | TEXT | Risk classification |

## 6. fact_aum (AUM by Fund House)
| Column | Type | Description |
|--------|------|-------------|
| date | DATE | Quarter end date |
| fund_house | TEXT | AMC name |
| aum_lakh_crore | REAL | AUM in ₹ Lakh Crore |
| aum_crore | REAL | AUM in ₹ Crore |
| num_schemes | INTEGER | Number of active schemes |

## 7. fact_holdings (Portfolio Holdings)
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | FK → dim_fund |
| stock_symbol | TEXT | NSE stock symbol |
| stock_name | TEXT | Full company name |
| sector | TEXT | Industry sector |
| weight_pct | REAL | Portfolio weight in % |
| market_value_cr | REAL | Market value in ₹ Crore |
| current_price_inr | REAL | Stock price in ₹ |
| portfolio_date | DATE | Date of portfolio snapshot |

---
*Source: AMFI India, mfapi.in, Bluestock synthetic dataset*
*Last updated: June 2026*