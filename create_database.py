import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)
print(f"dim_fund loaded - {len(fund_master)} rows")

nav = pd.read_csv("data/processed/02_nav_history_clean.csv")
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
print(f"fact_nav loaded - {len(nav)} rows")

txn = pd.read_csv("data/processed/08_investor_transactions_clean.csv")
txn.to_sql("fact_transactions", engine, if_exists="replace", index=False)
print(f"fact_transactions loaded - {len(txn)} rows")

perf = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)
print(f"fact_performance loaded - {len(perf)} rows")

aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)
print(f"fact_aum loaded - {len(aum)} rows")

print("\nDatabase Created Successfully!")
