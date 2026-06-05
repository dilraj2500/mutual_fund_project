import pandas as pd
import os

folder_path = "data/raw"

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        filepath = os.path.join(folder_path, file)
        df = pd.read_csv(filepath)
        print("\n" + "="*60)
        print("FILE:", file)
        print("\nShape:")
        print(df.shape)
        print("\nColumns:")
        print(df.columns.tolist())
        print("\nData Types:")
        print(df.dtypes)
        print("\nFirst 5 Rows:")
        print(df.head())
        print("\nMissing Values:")
        print(df.isnull().sum())
