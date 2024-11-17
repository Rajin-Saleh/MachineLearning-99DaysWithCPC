# 99DaysWithCPC - Machine Learning

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset

file_path = "Day17/listings.csv"  # Make sure this is the correct path to your CSV file
df = pd.read_csv(file_path)

# Data Cleaning

df = df.dropna(
    subset=[
        "price",
        "neighbourhood_group_cleansed",
        "room_type",
        "bedrooms",
        "accommodates",
    ]
)

# price to numeric (removing the dollar signs and commas)

df["price"] = df["price"].replace({"\$": "", ",": ""}, regex=True).astype(float)

# columns to appropriate data types

df["availability_365"] = df["availability_365"].astype(int)
df["minimum_nights"] = df["minimum_nights"].astype(int)
df["accommodates"] = df["accommodates"].astype(int)
df["bedrooms"] = df["bedrooms"].astype(float)
df["bathrooms"] = df["bathrooms"].astype(float)

# Normal Overview: Distribution of Price

plt.figure(figsize=(10, 6))
sns.histplot(df["price"], bins=50, kde=True)
plt.title("Price Distribution of Listings")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Room Type Distribution

plt.figure(figsize=(8, 5))
sns.countplot(x="room_type", data=df, palette="Set2")
plt.title("Room Type Distribution")
plt.xlabel("Room Type")
plt.ylabel("Count")
plt.show()

# Price vs. Accommodates (Capacity)

plt.figure(figsize=(10, 6))
sns.scatterplot(x="accommodates", y="price", data=df, hue="room_type", palette="Set1")
plt.title("Price vs. Accommodates (Capacity)")
plt.xlabel("Accommodates")
plt.ylabel("Price")
plt.show()

# Price vs. Number of Bedrooms

plt.figure(figsize=(10, 6))
sns.scatterplot(x="bedrooms", y="price", data=df)
plt.title("Price vs. Number of Bedrooms")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Price")
plt.show()

# Boxplot: Price Distribution by Room Type

plt.figure(figsize=(10, 6))
sns.boxplot(x="room_type", y="price", data=df)
plt.title("Price Distribution by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Price")
plt.show()

# Correlation Heatmap

corr_matrix = df[
    [
        "price",
        "accommodates",
        "bedrooms",
        "bathrooms",
        "minimum_nights",
        "availability_365",
    ]
].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix")
plt.show()

#  Availability vs. Price

plt.figure(figsize=(10, 6))
sns.scatterplot(
    x="availability_365", y="price", data=df, hue="room_type", palette="Set1"
)
plt.title("Availability vs. Price")
plt.xlabel("Availability (365 days)")
plt.ylabel("Price")
plt.show()

# Price per Bedroom

df["price_per_bedroom"] = df["price"] / df["bedrooms"]
plt.figure(figsize=(10, 6))
sns.histplot(df["price_per_bedroom"], bins=30, kde=True)
plt.title("Price per Bedroom Distribution")
plt.xlabel("Price per Bedroom")
plt.ylabel("Frequency")
plt.show()

# Superhost Analysis (if available in data)

if "host_is_superhost" in df.columns:
    superhost_data = df[df["host_is_superhost"] == "t"]
    non_superhost_data = df[df["host_is_superhost"] == "f"]
    superhost_avg_price = superhost_data["price"].mean()
    non_superhost_avg_price = non_superhost_data["price"].mean()
    print(f"Average Price for Superhosts: {superhost_avg_price}")
    print(f"Average Price for Non-Superhosts: {non_superhost_avg_price}")

# Outlier Detection: Price Boxplot

plt.figure(figsize=(10, 6))
sns.boxplot(x=df["price"])
plt.title("Price Outlier Detection")
plt.xlabel("Price")
plt.show()

# Price vs. Review Scores

if "review_scores_rating" in df.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="review_scores_rating", y="price", data=df)
    plt.title("Price vs. Review Scores Rating")
    plt.xlabel("Review Scores Rating")
    plt.ylabel("Price")
    plt.show()
