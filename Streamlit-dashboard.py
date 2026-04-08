import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Real-Time Sales Dashboard", layout="wide")

st.title("📡 Real-Time Sales Monitoring Dashboard")

# Auto-refresh every 5 seconds
REFRESH_INTERVAL = 5

# Function to load live transactions
def load_data():
    try:
        df = pd.read_csv("data/live_transactions.csv")
        return df
    except FileNotFoundError:
        st.warning("No live transactions found yet. Start the streaming generator.")
        return pd.DataFrame()

# Main loop
placeholder = st.empty()

while True:
    df = load_data()
    if not df.empty:
        # KPIs
        total_revenue = df["Revenue"].sum()
        total_expenses = df["Expenses"].sum()
        total_profit = total_revenue - total_expenses
        total_customers = df["Customers"].sum()

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
        col2.metric("📉 Total Expenses", f"${total_expenses:,.2f}")
        col3.metric("📈 Total Profit", f"${total_profit:,.2f}")
        col4.metric("👥 Customers", f"{total_customers:,}")

        # Charts
        st.subheader("Revenue by Region")
        st.bar_chart(df.groupby("Region")["Revenue"].sum())

        st.subheader("Revenue by Product")
        st.bar_chart(df.groupby("Product")["Revenue"].sum())

        st.subheader("Live Transactions")
        st.dataframe(df.tail(10))

        # Alerts
        if total_expenses > total_revenue:
            st.error("⚠️ Alert: Expenses exceed Revenue!")
        else:
            st.success("✅ Revenue is healthy compared to Expenses.")

    time.sleep(REFRESH_INTERVAL)
