# 99DaysWithCPC - Machine Learning

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Load the CSV
df = pd.read_csv("Day13/Projects/train.csv")

# Cleaning, Preprocessing

print("Number of missing values in each column:")
print(df.isnull().sum())

# date columns to datetime

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

print("Number of missing values in date columns after conversion:")
print(df[["Order Date", "Ship Date"]].isnull().sum())

# derived columns

df["Days to Ship"] = (df["Ship Date"] - df["Order Date"]).dt.days

# Single PDF to store all figures

with PdfPages("sales_data_analysis.pdf") as pdf:
    # Sales by Region

    sales_by_region = df.groupby("Region")["Sales"].sum().reset_index()
    sales_by_region = sales_by_region.sort_values("Sales", ascending=False)

    fig, ax = plt.subplots(figsize=(12, 6))
    sales_by_region.plot(kind="bar", x="Region", y="Sales", ax=ax, legend=False)
    ax.set_title("Sales by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Sales")
    pdf.savefig(fig)  # Save to PDF
    plt.show()  # Show plot on screen
    plt.close(fig)

    # Sales by Product Category

    sales_by_category = df.groupby("Category")["Sales"].sum().reset_index()
    sales_by_category = sales_by_category.sort_values("Sales", ascending=False)

    fig, ax = plt.subplots(figsize=(12, 6))
    sales_by_category.plot(kind="bar", x="Category", y="Sales", ax=ax, legend=False)
    ax.set_title("Sales by Product Category")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Sales")
    pdf.savefig(fig)  # Save to PDF
    plt.show()  # Show plot on screen
    plt.close(fig)

    # Sales Trends over Time

    fig, ax = plt.subplots(figsize=(12, 6))
    df.groupby(pd.Grouper(key="Order Date", freq="M"))["Sales"].sum().plot(
        kind="line", ax=ax
    )
    ax.set_title("Sales Trends Over Time")
    ax.set_xlabel("Order Date")
    ax.set_ylabel("Sales")
    pdf.savefig(fig)  # Save to PDF
    plt.show()  # Show plot on screen
    plt.close(fig)

    # Customer Segmentation Analysis

    sales_by_segment = df.groupby("Segment")["Sales"].mean().reset_index()
    sales_by_segment = sales_by_segment.sort_values("Sales", ascending=False)

    fig, ax = plt.subplots(figsize=(12, 6))
    sales_by_segment.plot(kind="bar", x="Segment", y="Sales", ax=ax, legend=False)
    ax.set_title("Average Sales by Customer Segment")
    ax.set_xlabel("Customer Segment")
    ax.set_ylabel("Average Sales")
    pdf.savefig(fig)  # Save to PDF
    plt.show()  # Show plot
    plt.close(fig)

print('PDF report "sales_data_analysis.pdf" has been generated.')
