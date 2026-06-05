import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            nav_df = pd.DataFrame(data["data"])
            nav_df["amfi_code"] = code
            nav_df["scheme_name"] = data["meta"]["scheme_name"]
            output_file = f"data/raw/{name}_live_nav.csv"
            nav_df.to_csv(output_file, index=False)
            print(f"SUCCESS: {name} saved - {len(nav_df)} rows")
        else:
            print(f"FAILED: {name} - Status {response.status_code}")
    except Exception as e:
        print(f"ERROR: {name} -> {e}")
