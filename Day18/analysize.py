# 99DaysWithCPC - Machine Learning

# Importing necessary libraries for the analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Reading the IKEA dataset

file_path = "Day18/ikea2.csv"
ikea_df = pd.read_csv(file_path)

# Cleaning and processing the data

ikea_df.columns = ikea_df.columns.str.strip()  # Remove extra spaces in column names
ikea_df["price"] = pd.to_numeric(
    ikea_df["price"], errors="coerce"
)  # Convert price to numeric
ikea_df["old_price"] = ikea_df["old_price"].replace(
    "No old price", np.nan
)  # Replace 'No old price' with NaN
ikea_df["old_price"] = pd.to_numeric(
    ikea_df["old_price"], errors="coerce"
)  # Convert old_price to numeric

# General Overview

total_products = len(ikea_df)
categories_count = ikea_df["category"].nunique()
designers_count = ikea_df["designer"].nunique()
status_count = ikea_df["current_status"].nunique()

print(f"Total Products: {total_products}")
print(f"Number of Categories: {categories_count}")
print(f"Number of Designers: {designers_count}")
print(f"Number of Status Types: {status_count}")

# Price Analysis

plt.figure(figsize=(20, 18))
sns.histplot(ikea_df["price"], kde=True, color="blue", bins=30)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Products with old_price and price difference

ikea_df["price_difference"] = ikea_df["old_price"] - ikea_df["price"]
old_price_products = ikea_df[ikea_df["price_difference"].notnull()]
print(f"Number of Products with Old Prices: {len(old_price_products)}")

# Category Insights

category_count = ikea_df["category"].value_counts()
avg_price_per_category = ikea_df.groupby("category")["price"].mean()

plt.figure(figsize=(20, 18))
sns.barplot(x=category_count.index, y=category_count.values, palette="viridis")
plt.title("Number of Products per Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.show()

# Online Sales Analysis

online_sales_dist = ikea_df["sellable_online"].value_counts(normalize=True)
online_vs_offline_prices = ikea_df.groupby("sellable_online")["price"].mean()

plt.figure(figsize=(18, 18))
online_sales_dist.plot(kind="pie", autopct="%1.1f%%", colors=["skyblue", "lightgreen"])
plt.title("Proportion of Products Sellable Online")
plt.ylabel("")
plt.show()

# Dimensional Analysis

dimensional_heatmap = ikea_df.pivot_table(
    index="category", values=["depth", "height", "width"], aggfunc="mean"
)
plt.figure(figsize=(20, 18))
sns.heatmap(dimensional_heatmap, annot=True, fmt=".1f", cmap="coolwarm")
plt.title("Average Dimensions by Category")
plt.show()

# Designer Popularity

designer_product_count = ikea_df["designer"].value_counts()
avg_price_per_designer = ikea_df.groupby("designer")["price"].mean()

plt.figure(figsize=(20, 18))
sns.barplot(
    x=designer_product_count.head(20).index,
    y=designer_product_count.head(20).values,
    palette="magma",
)
plt.title("Top 20 Designers by Number of Products")
plt.xlabel("Designer")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.show()

# Word Clouds

short_description_text = " ".join(ikea_df["short_description"].dropna().astype(str))
product_description_text = " ".join(ikea_df["product_description"].dropna().astype(str))

wordcloud = WordCloud(background_color="white", width=800, height=400).generate(
    short_description_text
)
plt.figure(figsize=(20, 18))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Short Descriptions")
plt.show()
