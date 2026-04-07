import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Business Insights Dashboard", layout="wide")

st.title("Business Insights Dashboard")
st.markdown("Interactive analytics dashboard for revenue trends, anomalies, forecasting, and AI-generated insights.")

# Load data
df = pd.read_csv("data/transactions_clean.csv")
forecast = pd.read_csv("data/forecast.csv")
anomalies = pd.read_csv("data/anomalies.csv")

# KPIs
total_revenue = df["revenue"].sum()
top_product = df.groupby("product")["revenue"].sum().idxmax()
top_region = df.groupby("region")["revenue"].sum().idxmax()
anomaly_count = len(anomalies)

# Revenue by product
product_revenue = df.groupby("product")["revenue"].sum().sort_values(ascending=False)

# Revenue by region
region_revenue = df.groupby("region")["revenue"].sum().sort_values(ascending=False)

# Daily revenue trend
df["date"] = pd.to_datetime(df["date"])
daily_revenue = df.groupby("date")["revenue"].sum().reset_index()

# KPI section
st.subheader("📌 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Top Product", top_product)
col3.metric("Top Region", top_region)
col4.metric("Anomalies Detected", anomaly_count)

st.markdown("---")

# Charts row 1
col5, col6 = st.columns(2)

with col5:
    st.subheader("Revenue by Product")
    fig, ax = plt.subplots(figsize=(6, 4))
    product_revenue.plot(kind="bar", ax=ax)
    ax.set_xlabel("Product")
    ax.set_ylabel("Revenue")
    ax.set_title("Revenue by Product")
    st.pyplot(fig)

with col6:
    st.subheader("Revenue by Region")
    fig, ax = plt.subplots(figsize=(6, 4))
    region_revenue.plot(kind="bar", ax=ax)
    ax.set_xlabel("Region")
    ax.set_ylabel("Revenue")
    ax.set_title("Revenue by Region")
    st.pyplot(fig)

st.markdown("---")

# Charts row 2
col7, col8 = st.columns(2)

with col7:
    st.subheader("Daily Revenue Trend")
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(daily_revenue["date"], daily_revenue["revenue"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue")
    ax.set_title("Daily Revenue Trend")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col8:
    st.subheader("Forecast (Next 30 Days)")
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(forecast["predicted_revenue"])
    ax.set_xlabel("Future Day")
    ax.set_ylabel("Predicted Revenue")
    ax.set_title("Forecasted Revenue")
    st.pyplot(fig)

st.markdown("---")

# Anomalies section
st.subheader("Sample Anomalies")
st.dataframe(anomalies.head(20), use_container_width=True)

st.markdown("---")

# Insights section
st.subheader("AI Insights")
try:
    with open("data/genai_insights.txt", "r") as f:
        insights = f.read()
    st.text_area("Generated Insights", insights, height=250)
except FileNotFoundError:
    st.warning("No insights file found.")