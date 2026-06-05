import pandas as pd
import numpy as np
import os

RAW = "data/raw"
PROCESSED = "data/processed"
os.makedirs(PROCESSED, exist_ok=True)

print("="*60)
print("CLEANING NAV HISTORY")
print("="*60)
nav = pd.read_csv(f"{RAW}/02_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"], errors="coerce")
nav = nav.dropna(subset=["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()
nav = nav.drop_duplicates(subset=["amfi_code","date"])
nav = nav[nav["nav"] > 0]
nav.to_csv(f"{PROCESSED}/02_nav_history_clean.csv", index=False)
print(f"Rows before: 46000 | Rows after: {len(nav)}")
print(f"Date range: {nav['date'].min()} to {nav['date'].max()}")
print(f"Missing NAV: {nav['nav'].isnull().sum()}")
print("NAV History DONE\n")

print("="*60)
print("CLEANING INVESTOR TRANSACTIONS")
print("="*60)
txn = pd.read_csv(f"{RAW}/08_investor_transactions.csv")
print(f"Original transaction_type values: {txn['transaction_type'].unique()}")
txn["transaction_type"] = txn["transaction_type"].astype(str).str.strip().str.title()
txn["transaction_type"] = txn["transaction_type"].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"], errors="coerce")
txn = txn.dropna(subset=["transaction_date"])
txn = txn[txn["amount_inr"] > 0]
valid_kyc = ["Verified", "Pending", "Rejected"]
print(f"KYC Status values: {txn['kyc_status'].unique()}")
txn = txn[txn["kyc_status"].isin(valid_kyc)]
txn.to_csv(f"{PROCESSED}/08_investor_transactions_clean.csv", index=False)
print(f"Rows after cleaning: {len(txn)}")
print(f"Transaction types: {txn['transaction_type'].unique()}")
print("Transactions DONE\n")

print("="*60)
print("CLEANING SCHEME PERFORMANCE")
print("="*60)
perf = pd.read_csv(f"{RAW}/07_scheme_performance.csv")
return_cols = ["return_1yr_pct", "return_3yr_pct", "return_5yr_pct"]
for col in return_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")
anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]
print(f"Expense ratio anomalies found: {len(anomalies)}")
if len(anomalies) > 0:
    print(anomalies[["scheme_name","expense_ratio_pct"]])
print(f"Return null values: {perf[return_cols].isnull().sum().to_dict()}")
perf.to_csv(f"{PROCESSED}/07_scheme_performance_clean.csv", index=False)
print(f"Rows after cleaning: {len(perf)}")
print("Scheme Performance DONE\n")

print("="*60)
print("COPYING OTHER CSVs TO PROCESSED")
print("="*60)
other_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]
for f in other_files:
    df = pd.read_csv(f"{RAW}/{f}")
    df.to_csv(f"{PROCESSED}/{f}", index=False)
    print(f"  Copied {f} — {len(df)} rows")

print("\nALL CLEANING DONE!")
print(f"Processed files in: {PROCESSED}/")