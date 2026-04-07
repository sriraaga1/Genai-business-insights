import pandas as pd
from sklearn.ensemble import IsolationForest

print("Loading cleaned dataset...")

df = pd.read_csv("data/transactions_clean.csv")

model = IsolationForest(contamination=0.01)

df["anomaly"] = model.fit_predict(df[["revenue"]])

anomalies = df[df["anomaly"] == -1]

print("Total rows:", len(df))
print("Anomalies detected:", len(anomalies))

anomalies.to_csv("data/anomalies.csv", index=False)

print("Anomaly detection completed")