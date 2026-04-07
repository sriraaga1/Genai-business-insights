import pandas as pd
from sklearn.linear_model import LinearRegression

print("Loading cleaned dataset...")

df = pd.read_csv("data/transactions_clean.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Aggregate revenue per day
daily_sales = df.groupby("date")["revenue"].sum().reset_index()

# Create time index
daily_sales["day_number"] = range(len(daily_sales))

# Model
X = daily_sales[["day_number"]]
y = daily_sales["revenue"]

model = LinearRegression()
model.fit(X, y)

# Predict next 30 days
future_days = pd.DataFrame({
    "day_number": range(len(daily_sales), len(daily_sales) + 30)
})

future_predictions = model.predict(future_days)

# Save forecast
forecast_df = future_days.copy()
forecast_df["predicted_revenue"] = future_predictions

forecast_df.to_csv("data/forecast.csv", index=False)

print("Forecasting completed successfully")