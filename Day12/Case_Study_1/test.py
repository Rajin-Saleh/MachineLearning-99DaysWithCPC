# 99DaysWithCPC - Machine Learning

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading the dataset

data = pd.read_csv(
    "Day12/Case_Study_1/Ecommerce_Purchases"
)  # Replace with your actual file name if different

# Display the first few rows of data for an overview

print("Data Sample:")
print(data.head())

# Checking missing values and data types

print("\nMissing Values in Each Column:")
print(data.isnull().sum())

# if needed (e.g., `CC Exp Date` to DateTime for expiry analysis)

data["CC Exp Date"] = pd.to_datetime(data["CC Exp Date"], errors="coerce")

# `Purchase Price` to numeric if not already

data["Purchase Price"] = pd.to_numeric(data["Purchase Price"], errors="coerce")

# User Demographics Analysis

# Analyze AM or PM purchases

am_pm_counts = data["AM or PM"].value_counts()
print("\nAM vs PM Purchase Distribution:")
print(am_pm_counts)

# Common job roles

top_jobs = data["Job"].value_counts().nlargest(10)
print("\nTop 10 Job Titles of Customers:")
print(top_jobs)

# Preferred language counts

language_counts = data["Language"].value_counts()
print("\nPreferred Language Distribution:")
print(language_counts)

# Purchasing Behavior Analysis

# Average Purchase Price

average_price = data["Purchase Price"].mean()
print(f"\nAverage Purchase Price: ${average_price:.2f}")

# Top 10 companies by average purchase price

top_companies_by_purchase = (
    data.groupby("Company")["Purchase Price"].mean().nlargest(10)
)
print("\nTop 10 Companies by Average Purchase Price:")
print(top_companies_by_purchase)

# Visualizing the Purchase Price Distribution

plt.figure(figsize=(10, 6))
plt.hist(data["Purchase Price"].dropna(), bins=20, color="skyblue", edgecolor="black")
plt.title("Purchase Price Distribution")
plt.xlabel("Purchase Price ($)")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Visualizing the Purchase Prices by Company

plt.figure(figsize=(12, 8))
top_companies_by_purchase.plot(kind="bar", color="teal", edgecolor="black")
plt.title("Top 10 Companies by Average Purchase Price")
plt.xlabel("Company")
plt.ylabel("Average Purchase Price ($)")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Anomaly Detection

# High purchase prices (potential anomalies)

high_price_threshold = data["Purchase Price"].mean() + 3 * data["Purchase Price"].std()
anomalous_purchases = data[data["Purchase Price"] > high_price_threshold]
print("\nAnomalies in Purchase Price (Above Threshold):")
print(anomalous_purchases[["Company", "Purchase Price"]])

# Expired credit cards

current_year = pd.Timestamp.now().year
data["CC Exp Year"] = data["CC Exp Date"].dt.year
expired_cards = data[data["CC Exp Year"] < current_year]
print("\nExpired Credit Cards:")
print(expired_cards[["Email", "Credit Card", "CC Exp Date"]])

# Summary Output for PDF Report

summary = {
    "Average Purchase Price": f"${average_price:.2f}",
    "Top 10 Companies by Average Purchase Price": top_companies_by_purchase.to_dict(),
    "Anomalous Purchases (High Price)": anomalous_purchases[
        ["Company", "Purchase Price"]
    ].to_dict(orient="records"),
    "Expired Credit Cards": expired_cards[
        ["Email", "Credit Card", "CC Exp Date"]
    ].to_dict(orient="records"),
}

# for report generation

print("\nSummary for PDF Report:")
print(summary)
