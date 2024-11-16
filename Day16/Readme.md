# 99DaysWithCPC - Machine Learning

Data analyzing Project

# Body Metrics and Fashion Colors Data Analysis

## Overview

This project analyzes a dataset containing body metrics and fashion color data, with attributes such as height, weight, BMI, gender, and color preferences (skin, clothes, and pants colors). The goal is to perform descriptive analysis, explore relationships between different attributes, and visualize the data through various plots. The project also generates a comprehensive PDF report summarizing the analysis and visualizations.

### Dataset Information

The dataset includes the following columns:

- **Height (Centimeter)**: The height of the individual in centimeters.
- **Weight (Kilograms)**: The weight of the individual in kilograms.
- **Gender**: The gender of the individual (Male/Female).
- **BMI**: The Body Mass Index category (Underweight, Ideal, Overweight, etc.).
- **Skin Color**: The RGB color values representing the skin color.
- **Clothes Color**: The RGB color values representing the clothes color.
- **Pants Color**: The RGB color values representing the pants color.

### Project Objectives

The main objectives of this project are:

- **Data Cleaning and Preprocessing**: Ensure proper formatting and parsing of the dataset, including handling color columns stored as RGB tuples.
- **Descriptive Statistics**: Generate statistical summaries (mean, standard deviation) for numerical columns.
- **Correlation Analysis**: Analyze correlations between height, weight, and BMI.
- **Data Visualization**: Create several visualizations, including scatter plots, bar charts, and heatmaps to explore relationships in the data.
- **PDF Report Generation**: Summarize the findings and visualizations in a PDF report.

## Getting Started

### Prerequisites

To run the project, you'll need the following Python libraries:

- pandas
- numpy
- matplotlib
- seaborn
- fpdf

You can install the required dependencies by running:

```bash
pip install pandas numpy matplotlib seaborn fpdf

File Structure

Body_Metrics_Analysis/
│
├── Day16/Profile_of_Body_Metrics_and_Fashion_Colors.csv    # Dataset file
├── data_analysis_report.pdf                                 # PDF report with analysis and visualizations
├── scatter_height_weight.png                                # Scatter plot image
├── bar_bmi_gender.png                                      # Bar plot image
├── correlation_heatmap.png                                  # Correlation heatmap image
├── test.py                                                 # Python script for data analysis
├── README.md                                               # This README file

Running the Analysis

To run the data analysis script and generate the PDF report, follow these steps:

    Ensure your dataset is in the correct location (Day16/Profile_of_Body_Metrics_and_Fashion_Colors.csv).
    Run the Python script:

python test.py

The script will generate:

    Descriptive statistics for the numerical columns.
    Three visualizations:
        A scatter plot of height vs. weight, colored by BMI.
        A bar plot showing the BMI categories by gender.
        A heatmap of the correlation between height and weight.
    A PDF report (data_analysis_report.pdf) summarizing the analysis and including the visualizations.

Example Output

Here’s a brief overview of the expected outputs:

    Descriptive Statistics: Summary of mean and standard deviation for height, weight, and BMI.
    Scatter Plot: A scatter plot showing the relationship between height and weight, with different colors representing BMI categories.
    Bar Plot: A bar plot that illustrates the BMI categories for each gender.
    Correlation Heatmap: A heatmap showing the correlation between height and weight.

Report Generation

After running the script, a PDF report will be created with the following sections:

    Title: "Data Analysis Report"
    Descriptive Statistics: A table showing mean and standard deviation for each numerical column.
    Visualizations: Three images:
        Height vs. Weight Scatter Plot
        BMI Categories by Gender Bar Plot
        Correlation Heatmap

Conclusion

This project offers insights into body metrics and fashion color data by applying descriptive analysis and data visualization techniques. The generated PDF report serves as a concise summary of the analysis, which can be useful for further exploration or presentation purposes.
