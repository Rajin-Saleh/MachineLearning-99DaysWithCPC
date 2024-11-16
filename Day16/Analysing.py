# 99DaysWithCPC - Machine Learning

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

# Dataset

file_path = "Day16/Profile_of_Body_Metrics_and_Fashion_Colors.csv"  # Replace with the correct file path


try:
    # Read the CSV file
    data = pd.read_csv(file_path, delimiter=";")
except FileNotFoundError:
    print(f"File not found at {file_path}. Please ensure the file exists.")
    raise

# Clean column names (strip extra spaces if any)

data.columns = data.columns.str.strip()

# Skin, Clothes, Pants


def parse_color(color_str):
    try:
        return tuple(map(int, color_str.strip("()").split(", ")))
    except Exception as e:
        print(f"Error parsing color: {color_str} -> {e}")
        return (0, 0, 0)


data["Skin Color"] = data["Skin Color"].apply(parse_color)
data["Clothes Color"] = data["Clothes Color"].apply(parse_color)
data["Pants Color"] = data["Pants Color"].apply(parse_color)

# columns and data types

print("Columns in the dataset:", data.columns)
print("Data Types:", data.dtypes)

# statistics for numerical columns

stats = data.describe()

# Check if 'mean' and 'std' are available

if "mean" not in stats.index or "std" not in stats.index:
    print(
        "Descriptive statistics missing 'mean' or 'std'. Check the dataset's numerical columns."
    )
else:
    # Access and print descriptive statistics
    print("Descriptive statistics:", stats)

# Correlation matrix

correlation = data[["Height(Centimeter)", "Weight(Kilograms)"]].corr()

# Scatter : Height vs Weight

plt.figure(figsize=(8, 6))
sns.scatterplot(
    x="Height(Centimeter)",
    y="Weight(Kilograms)",
    hue="BMI",
    data=data,
    alpha=0.6,
    palette="Set2",
)
plt.title("Height vs Weight by BMI Category")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.savefig("scatter_height_weight.png")
plt.show()
plt.close()

# Bar: BMI categories by Gender

bmi_gender_counts = data.groupby(["Gender", "BMI"]).size().unstack()
bmi_gender_counts.plot(kind="bar", stacked=True, figsize=(8, 6), colormap="viridis")
plt.title("BMI Categories by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.savefig("bar_bmi_gender.png")
plt.show()
plt.close()

# Heatmap: Correlation matrix

plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()
plt.close()

# PDF report making

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add title

pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align="C")

# Add descriptive statistics

pdf.set_font("Arial", size=10)
pdf.cell(0, 10, txt="Descriptive Statistics:", ln=True)
for col in stats.columns:
    mean = stats.loc["mean", col] if "mean" in stats.index else "N/A"
    std = stats.loc["std", col] if "std" in stats.index else "N/A"
    pdf.cell(0, 10, txt=f"{col}: Mean = {mean}, Std = {std}", ln=True)

# images into pdf

pdf.add_page()
pdf.cell(0, 10, txt="Height vs Weight Scatter Plot", ln=True)
pdf.image("scatter_height_weight.png", x=10, y=None, w=180)

pdf.add_page()
pdf.cell(0, 10, txt="BMI Categories by Gender Bar Plot", ln=True)
pdf.image("bar_bmi_gender.png", x=10, y=None, w=180)

pdf.add_page()
pdf.cell(0, 10, txt="Correlation Heatmap", ln=True)
pdf.image("correlation_heatmap.png", x=10, y=None, w=180)

# Saving the PDF
pdf.output("data_analysis_report.pdf")
print("PDF report has been generated and saved as 'data_analysis_report.pdf'.")
