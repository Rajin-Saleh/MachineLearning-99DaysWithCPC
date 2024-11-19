# 99DaysWithCPC - Machine Learning


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

df = pd.read_csv("Day19/plant_health_data.csv")


# Clean and Inspect Data

print("Data Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# Convert Timestamp to datetime type

df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
df = df.dropna(subset=["Timestamp"])

# Data Exploration

print("\nBasic Statistics:\n", df.describe())


# Create a function to set common plot styles


def set_plot_style():
    plt.style.use("seaborn")
    plt.rcParams["figure.figsize"] = (12, 6)
    plt.rcParams["font.size"] = 10
    plt.rcParams["axes.labelsize"] = 12
    plt.rcParams["axes.titlesize"] = 14


# Distribution of Plant Health Status

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Plant_Health_Status")
plt.title("Distribution of Plant Health Status")
plt.xlabel("Health Status")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.close()

# Correlation Heatmap

environmental_factors = [
    "Soil_Moisture",
    "Ambient_Temperature",
    "Soil_Temperature",
    "Humidity",
    "Light_Intensity",
    "Soil_pH",
    "Nitrogen_Level",
    "Phosphorus_Level",
    "Potassium_Level",
    "Chlorophyll_Content",
    "Electrochemical_Signal",
]

corr_matrix = df[environmental_factors].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=1)
plt.title("Correlation Heatmap of Environmental Factors")
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
plt.close()

# Time-Based Analysis
# Resample data to daily averages for smoother plotting

df["Date"] = df["Timestamp"].dt.date
daily_avg = (
    df.groupby("Date")
    .agg(
        {
            "Soil_Moisture": "mean",
            "Ambient_Temperature": "mean",
            "Soil_Temperature": "mean",
        }
    )
    .reset_index()
)

fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(
    daily_avg["Date"], daily_avg["Soil_Moisture"], label="Soil Moisture", marker="o"
)
ax.plot(
    daily_avg["Date"],
    daily_avg["Ambient_Temperature"],
    label="Ambient Temperature",
    marker="s",
)
ax.plot(
    daily_avg["Date"],
    daily_avg["Soil_Temperature"],
    label="Soil Temperature",
    marker="^",
)
ax.set_title("Environmental Factors Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Values")
ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.close()

# Plant Health vs Environmental Factors

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle("Plant Health Status vs Environmental Factors", fontsize=16)

# Chlorophyll Content

sns.boxplot(x="Plant_Health_Status", y="Chlorophyll_Content", data=df, ax=axes[0, 0])
axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=45)
axes[0, 0].set_title("Chlorophyll Content")

# Soil Moisture

sns.boxplot(x="Plant_Health_Status", y="Soil_Moisture", data=df, ax=axes[0, 1])
axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=45)
axes[0, 1].set_title("Soil Moisture")

# Nitrogen Level

sns.boxplot(x="Plant_Health_Status", y="Nitrogen_Level", data=df, ax=axes[1, 0])
axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=45)
axes[1, 0].set_title("Nitrogen Level")

# Light Intensity

sns.boxplot(x="Plant_Health_Status", y="Light_Intensity", data=df, ax=axes[1, 1])
axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=45)
axes[1, 1].set_title("Light Intensity")

plt.tight_layout()
plt.show()
plt.close()

# Summary Statistics by Health Status

health_summary = df.groupby("Plant_Health_Status")[environmental_factors].mean()
print("\nHealth Status Summary:\n")
print(health_summary.round(2).to_string())

# Save the new cleaned data

df.to_csv("Day19/cleaned_plant_health_data.csv", index=False)
print("\nAnalysis Complete. All visualizations should now be displayed.")
