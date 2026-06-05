import pandas as pd
import os

RAW = "data/raw"
PROCESSED = "data/processed"
os.makedirs(PROCESSED, exist_ok=True)

nav = pd.read_csv(f"{RAW}/02_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"], errors="coerce")
nav = nav.sort_values(["amfi_code", "date"])
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()
nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]
nav.to_csv(f"{PROCESSED}/02_nav_history_clean.csv", index=False)
print(f"NAV cleaned - {len(nav)} rows")

txn = pd.read_csv(f"{RAW}/08_investor_transactions.csv")
txn["transaction_type"] = txn["transaction_type"].astype(str).str.strip().str.title()
txn["transaction_type"] = txn["transaction_type"].replace({"Sip": "SIP", "Lumpsum": "Lumpsum", "Redemption": "Redemption"})
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"], errors="coerce")
txn = txn[txn["amount_inr"] > 0]
txn.to_csv(f"{PROCESSED}/08_investor_transactions_clean.csv", index=False)
print(f"Transactions cleaned - {len(txn)} rows")

perf = pd.read_csv(f"{RAW}/07_scheme_performance.csv")
for col in ["return_1yr_pct", "return_3yr_pct", "return_5yr_pct"]:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")
perf.to_csv(f"{PROCESSED}/07_scheme_performance_clean.csv", index=False)
print(f"Performance cleaned - {len(perf)} rows")
