from dotenv import load_dotenv
import os
import pandas as pd
from openai import OpenAI

# Load variables from .env file
load_dotenv()

print("Loading project outputs...")

# Check whether API key is available
api_key = os.getenv("OPENAI_API_KEY")
print("API KEY FOUND:", api_key is not None)

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found. Please put your real key inside the .env file like this:\n"
        "OPENAI_API_KEY=sk-proj-xxxxxxxxxxxx"
    )

# Load project output files
transactions = pd.read_csv("data/transactions_clean.csv")
anomalies = pd.read_csv("data/anomalies.csv")
forecast = pd.read_csv("data/forecast.csv")

# Create summary metrics
total_revenue = transactions["revenue"].sum()
top_product = transactions.groupby("product")["revenue"].sum().idxmax()
top_region = transactions.groupby("region")["revenue"].sum().idxmax()
anomaly_count = len(anomalies)
avg_forecast = forecast["predicted_revenue"].mean()

# Prompt for GPT
summary = f"""
Business dataset summary:
- Total revenue: {total_revenue:.2f}
- Top product by revenue: {top_product}
- Top region by revenue: {top_region}
- Total anomalies detected: {anomaly_count}
- Average predicted future daily revenue: {avg_forecast:.2f}

Please generate:
1. 5 business insights
2. 3 anomaly-related observations
3. 3 forecasting insights
4. 3 business recommendations

Keep the tone professional and concise.
"""

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Call GPT
response = client.responses.create(
    model="gpt-4.1-mini",
    input=summary
)

# Get output text
insights = response.output_text

# Save output
with open("data/genai_insights_gpt.txt", "w") as file:
    file.write(insights)

print("GPT-generated insights file created successfully")