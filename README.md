# 📡 Real-Time Sales Monitoring Dashboard

![Status](https://img.shields.io/badge/Project-Active-brightgreen)
![Tool](https://img.shields.io/badge/Python-Streamlit%20%7C%20Pandas%20%7C%20Matplotlib-blue)
![Focus](https://img.shields.io/badge/Domain-Real--Time%20Analytics-orange)

## 🚀 Objective
Build a **real-time monitoring dashboard** that displays live sales transactions, KPIs, and alerts.  
This project demonstrates how streaming data can be transformed into actionable insights for fast decision-making.

---

## 🛠️ Workflow
1. **Data Streaming**  
   - `streaming_generator.py` simulates live sales transactions every few seconds.  
   - Transactions include: Timestamp, Region, Product, Revenue, Expenses, Customers.  
   - Data is continuously saved to `live_transactions.csv`.

2. **Dashboard Visualization**  
   - `streamlit_dashboard.py` reads the live dataset.  
   - Displays KPIs: Revenue, Expenses, Profit, Customers.  
   - Interactive charts: Revenue by Region, Revenue by Product.  
   - Alerts when Expenses exceed Revenue.

3. **Automation**  
   - Dashboard auto-refreshes every 5 seconds.  
   - Can be deployed locally (`streamlit run streamlit_dashboard.py`) or hosted on Streamlit Cloud.

---

## 📂 Deliverables
- `/data` → Live transactions dataset (`live_transactions.csv`).  
- `/scripts` → Streaming generator and Streamlit dashboard scripts.  
- `/dashboard` → Streamlit app files + screenshots.  
- `/insights` → Markdown file summarizing business impact of real-time monitoring.  
- `README.md` → Documentation (this file).  

---

## 🔍 Business Value
- **Real-Time Visibility** → Monitor KPIs as transactions occur.  
- **Proactive Alerts** → Detect overspending or anomalies instantly.  
- **Decision Support** → Enables faster responses to operational challenges.  

---

## 📸 Example Workflow
*(Insert screenshots of Streamlit dashboard with live KPIs and charts here)*

---

## 🧭 Next Steps
- Integrate with actual streaming sources (Kafka, Azure Event Hub).  
- Add predictive alerts (e.g., anomaly detection).  
- Deploy dashboard for enterprise use with authentication and role-based access.
