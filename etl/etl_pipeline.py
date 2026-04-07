import pandas as pd

print("Loading raw dataset...")

df = pd.read_csv("data/transactions_raw.csv")

print("Rows before cleaning:", len(df))

# Remove missing values
df.dropna(inplace=True)

# Convert date column into proper date format
df["date"] = pd.to_datetime(df["date"])

# Create useful columns
df["month"] = df["date"].dt.month
df["weekday"] = df["date"].dt.day_name()

# Validate revenue
df["revenue_check"] = df["quantity"] * df["price"]

# Keep only rows where revenue is correct
df = df[df["revenue"] == df["revenue_check"]]

# Remove helper column
df.drop("revenue_check", axis=1, inplace=True)

print("Rows after cleaning:", len(df))

# Save cleaned dataset
df.to_csv("data/transactions_clean.csv", index=False)

print("ETL pipeline completed successfully")
