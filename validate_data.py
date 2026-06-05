import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])
missing_codes = fund_codes - nav_codes

print("="*50)
print("DATA QUALITY SUMMARY")
print("="*50)
print(f"Fund Master Schemes     : {len(fund_codes)}")
print(f"NAV History Schemes     : {len(nav_codes)}")
print(f"Missing AMFI Codes      : {len(missing_codes)}")

if len(missing_codes) > 0:
    print("\nMissing Codes:")
    print(missing_codes)
else:
    print("\nAll AMFI codes present in NAV history.")

print(f"\nNAV History Total Rows  : {len(nav_history)}")
print(f"NAV Date Range          : {nav_history['date'].min()} to {nav_history['date'].max()}")
print(f"Duplicate NAV Rows      : {nav_history.duplicated().sum()}")
print(f"Missing NAV Values      : {nav_history['nav'].isnull().sum()}")
