# Fraud Detection Analysis Project

## Project Overview

This project aims to explore patterns in a dataset containing information on individuals’ professions, income, credit card details, and fraud status. Through data exploration and visualization, we seek to understand potential correlations between fraud and various features such as profession and income.

## Dataset Information

- **File**: `Fraud_Data.csv`
- **Columns**: Profession, Income, Credit_card_number, Expiry, Security_code, Fraud

The dataset includes sensitive data; thus, personal details like `Credit_card_number` and `Security_code` were masked for privacy in our analysis.

## Analysis Steps

1. **Data Preparation**:
   - Dropped sensitive fields (`Credit_card_number` and `Security_code`).
   - Converted `Expiry` to a datetime format for time-based analysis.

2. **Analysis of Fraud Trends**:
   - **Income by Profession**: Bar chart to compare average income across professions.
   - **Fraud Proportion**: Pie chart showing fraud vs. non-fraud cases.
   - **Fraud Rate by Profession**: Count plot of fraud cases within each profession.
   - **Correlation Matrix**: Heatmap to show the correlation between `Income` and `Fraud`.
   - **Expiry Date Insights**: Histogram of expiry years to detect any relation between card expiration dates and fraud incidents.

3. **Visualizations**:
   - **Income by Profession** - Highlights income distribution across different professions.
   - **Fraud Proportion** - Pie chart to illustrate the share of fraud vs. non-fraud cases.
   - **Fraud by Profession** - Shows fraud frequency by profession.
   - **Correlation Heatmap** - Examines the relationship between fraud occurrences and income.
   - **Expiry Date Distribution** - Shows distribution of card expiry dates to spot trends related to fraud.

## How to Use

Run the `Fraud_Analysis.py` script to process the dataset and visualize the results. The code provides detailed explanations at each step, making it easy to understand and modify for further analysis.

## Dependencies

- `pandas`, `numpy`, `matplotlib`, `seaborn`
