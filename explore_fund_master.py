import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Shape:", df.shape)
print("\nUnique Fund Houses:")
print(df["fund_house"].unique())
print("\nUnique Categories:")
print(df["category"].unique())
print("\nUnique Sub Categories:")
print(df["sub_category"].unique())
print("\nUnique Risk Categories:")
print(df["risk_category"].unique())
print("\nScheme Count by Fund House:")
print(df["fund_house"].value_counts())
print("\nScheme Count by Category:")
print(df["category"].value_counts())
