import time
import random
import pandas as pd

# Simulated product categories and regions
products = ["SUV", "Sedan", "Hatchback", "Accessories"]
regions = ["North", "South", "East", "West"]

# Create an empty DataFrame to store transactions
columns = ["Timestamp", "Region", "Product", "Revenue", "Expenses", "Customers"]
transactions = pd.DataFrame(columns=columns)

def generate_transaction():
    """Simulate a single sales transaction."""
    timestamp = pd.Timestamp.now()
    region = random.choice(regions)
    product = random.choice(products)
    revenue = round(random.uniform(5000, 20000), 2)
    expenses = round(revenue * random.uniform(0.4, 0.8), 2)
    customers = random.randint(1, 5)
    return [timestamp, region, product, revenue, expenses, customers]

# Stream transactions in real-time
print("Starting live transaction stream... Press Ctrl+C to stop.")
while True:
    new_tx = generate_transaction()
    transactions.loc[len(transactions)] = new_tx
    print(f"New Transaction: {new_tx}")
    
    # Save to CSV so Streamlit dashboard can pick it up
    transactions.to_csv("data/live_transactions.csv", index=False)
    
    # Wait 3 seconds before next transaction
    time.sleep(3)
