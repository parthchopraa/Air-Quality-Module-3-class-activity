import pandas as pd
import numpy as np

# File path (put air_quality.csv in the same folder OR update the path)
path = r"C:\Users\vassu\PycharmProjects\PythonProject\air_quality.csv"

# Load dataset
df = pd.read_csv(path, sep=';')

# Drop useless columns
df = df.drop(columns=[c for c in df.columns if "Unnamed" in c], errors='ignore')

# Convert comma decimals to numeric
for col in df.columns:
    if col not in ["Date", "Time"]:
        df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", "."), errors='coerce')

# Replace invalid values (-200) with NaN
df.replace(-200, np.nan, inplace=True)

# Fill missing values using mean
num_cols = df.select_dtypes(include='number').columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Save cleaned file
out_path = r"C:\Users\vassu\PycharmProjects\PythonProject\air_quality_cleaned.csv"
df.to_csv(out_path, index=False)

print("✅ Missing values fixed.")
print("📁 Cleaned file saved at:", out_path)
