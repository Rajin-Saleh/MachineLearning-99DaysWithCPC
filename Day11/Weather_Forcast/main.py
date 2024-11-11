import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Step 1: Load CSV data
# Load the data using pandas, then convert necessary columns to numpy arrays
data = pd.read_csv("file.csv")
# Display first few rows to understand structure (optional)
print(data.head())

# Step 2: Extract data for analysis
# Convert columns to numpy arrays
dates = pd.to_datetime(data["Date/Time"])  # Convert Date/Time to datetime
temp = data["Temp_C"].values  # Temperature
humidity = data["Rel Hum_%"].values  # Humidity
weather_conditions = data["Weather"].values  # Weather condition descriptions

# Step 3: Calculate Max-Min Temperature Range
max_temp = np.max(temp)
min_temp = np.min(temp)
temp_range = max_temp - min_temp
print(
    f"Max Temperature: {max_temp}°C, Min Temperature: {min_temp}°C, Temperature Range: {temp_range}°C"
)

# Step 4: Calculate Monthly Averages (if data has multiple months)
# Group by month and calculate mean values for temperature and humidity
data["Month"] = dates.dt.month
monthly_avg_temp = data.groupby("Month")["Temp_C"].mean().values
monthly_avg_humidity = data.groupby("Month")["Rel Hum_%"].mean().values

# Step 5: Visualize Data
# Plot line chart for Temperature and Humidity trends
plt.figure(figsize=(10, 6))
plt.plot(dates, temp, label="Temperature (°C)", color="tab:blue", alpha=0.7)
plt.plot(dates, humidity, label="Humidity (%)", color="tab:orange", alpha=0.7)
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Temperature and Humidity Trends Over Time")
plt.legend()
plt.grid(True)
plt.show()

# Step 6: Plot pie chart for weather condition distribution
# Count each unique weather condition
weather_counts = data["Weather"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(weather_counts, labels=weather_counts.index, autopct="%1.1f%%", startangle=140)
plt.title("Weather Condition Distribution")
plt.show()

# Step 7: Output Summary
print("\nMonthly Average Temperature (°C):", monthly_avg_temp)
print("Monthly Average Humidity (%):", monthly_avg_humidity)
