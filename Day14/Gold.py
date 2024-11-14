import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
data_path = "Day14/Gold_Prices.csv"
df = pd.read_csv(data_path)

#  'Date' to datetime
df["Date"] = pd.to_datetime(df["Date"], utc=True).dt.tz_convert(None)

# columns on correct data type
df["Open"] = df["Open"].astype(float)
df["High"] = df["High"].astype(float)
df["Low"] = df["Low"].astype(float)
df["Close"] = df["Close"].astype(float)
df["Volume"] = df["Volume"].astype(float)

# Sorting by Date
df = df.sort_values("Date")

# Date as the index
df.set_index("Date", inplace=True)

# Daily Returns Calculation
df["Daily Return %"] = (df["Close"] - df["Open"]) / df["Open"] * 100

# Moving Averages (7-day and 30-day)
df["7-day MA"] = df["Close"].rolling(window=7).mean()
df["30-day MA"] = df["Close"].rolling(window=30).mean()

# Plot Close Price with Moving Averages
plt.figure(figsize=(14, 7))
plt.plot(df["Close"], label="Close Price", color="blue")
plt.plot(df["7-day MA"], label="7-day Moving Average", color="orange")
plt.plot(df["30-day MA"], label="30-day Moving Average", color="green")
plt.title("Gold Close Price and Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# Daily Return Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df.index, df["Daily Return %"], c="purple", alpha=0.5)
plt.title("Daily Return Percentage")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
plt.show()

# Volume Area Chart
plt.figure(figsize=(14, 6))
plt.fill_between(df.index, df["Volume"], color="skyblue", alpha=0.4)
plt.title("Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 6))
correlation_matrix = df[["Open", "High", "Low", "Close", "Volume"]].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", center=0)
plt.title("Price and Volume Correlation Matrix")
plt.show()

# Dividends, Stock Splits, and Capital Gains Analysis (if applicable)
dividends_total = df["Dividends"].sum()
splits_total = df["Stock Splits"].sum()
gains_total = df["Capital Gains"].sum()

# Pie chart if any values are non-zero
if dividends_total > 0 or splits_total > 0 or gains_total > 0:
    plt.figure(figsize=(8, 8))
    plt.pie(
        [dividends_total, splits_total, gains_total],
        labels=["Dividends", "Stock Splits", "Capital Gains"],
        autopct="%1.1f%%",
        startangle=140,
        colors=["#ff9999", "#66b3ff", "#99ff99"],
    )
    plt.title("Proportion of Dividends, Stock Splits, and Capital Gains")
    plt.show()
