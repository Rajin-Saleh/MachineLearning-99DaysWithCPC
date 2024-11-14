# Gold Price Analysis Project

## Project Overview

Analyzing the given gold price data historically, we get insights on daily returns, moving averages, trading volume, and other financial metrics. In this respect, different visualizations are done to understand the pattern of price movement of gold over time and to identify possible trends.

## Dataset Information

- **File**: `Gold_Prices.csv`
- **Columns**: Date, Open, High, Low, Close, Volume, Dividends, Stock Splits, Capital Gains

The dataset contains daily information on the opening and closing prices of gold, daily high and low prices, and trading volume, which can be used to make a full analysis regarding price trends and market activities.

## Analysis Steps

1. **Data Preprocessing**:

- Converted `Date` to datetime format, sorted and set as index for time-based analysis.
- Made sure that numeric columns (`Open`, `High`, `Low`, `Close`, `Volume`) were of type `float`.

2. **Daily Returns Calculation**:

- Calculated daily return percentages using the formula:
\[
\text{Daily Return %} = \frac{\text{Close - Open}}{\text{Open}} \times 100
:]

3. **Moving Averages**:

- Computed 7-day and 30-day moving averages of the close price for smoothing out short-term fluctuations.

4. **Visualizations**:

- **Close Price & Moving Averages Plot**: Line chart showing the daily close price and moving averages.
- **Daily Return Scatter Plot**: Plots daily return percentages over time.
- **Volume Area Chart**: Area chart indicating trading volume trends in time.
- **Correlation Heatmap**: Correlation matrix for `Open`, `High`, `Low`, `Close` and `Volume`.
Dividend, Stock Split, and Capital Gains Analysis (if non-zero values present).

## Visualizations

1. **Close Price & Moving Averages**: Helps to define the overall trends and support/resistance levels.

2. **Scatter Plot of Daily Returns**: Shows daily movements, highlighting periods of high volatility. 3. **Volume Area Chart** - Displays trading activity trends. 4. **Correlation Heatmap** — shows the relationships between price components. ## How to Use Execute `Gold_Analysis.py` file to generate all visualizations and perform the analysis on the dataset. The script has inbuilt comments explaining each step. ## Dependencies - `pandas`, `numpy`, `matplotlib`, `seaborn`