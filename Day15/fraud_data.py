import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# CSV file
data_path = "Day15/data2.csv"  # Update path
df = pd.read_csv(data_path)

# mask sensitive data
df = df.drop(columns=["Credit_card_number", "Security_code"])  # For privacy


df["Expiry"] = pd.to_datetime(df["Expiry"], format="%m/%y", errors="coerce")

# Income Analysis by Profession
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Profession", y="Income", ci=None, palette="viridis")
plt.title("Average Income by Profession")
plt.xlabel("Profession")
plt.ylabel("Average Income")
plt.show()

# Fraud Proportion
fraud_counts = df["Fraud"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(
    fraud_counts,
    labels=["Non-Fraud", "Fraud"],
    autopct="%1.1f%%",
    startangle=140,
    colors=["#ff9999", "#66b3ff"],
)
plt.title("Proportion of Fraud vs Non-Fraud Cases")
plt.show()

# Fraud Rate by Profession
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Profession", hue="Fraud", palette="pastel")
plt.title("Fraud Cases by Profession")
plt.xlabel("Profession")
plt.ylabel("Count")
plt.legend(title="Fraud")
plt.show()

# Correlation Heatmap (Income and Fraud)
df["Fraud"] = df["Fraud"].astype(float)  # Convert for correlation analysis
correlation_matrix = df[["Income", "Fraud"]].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", center=0)
plt.title("Correlation between Income and Fraud")
plt.show()

# Expiry Date Insights (if Fraud is time-sensitive)
plt.figure(figsize=(12, 6))
sns.histplot(df["Expiry"].dt.year.dropna(), bins=15, kde=True, color="teal")
plt.title("Distribution of Expiry Years")
plt.xlabel("Expiry Year")
plt.ylabel("Frequency")
plt.show()
