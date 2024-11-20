# 99DaysWitchCPC - Machine Learning

# %% [markdown]
# Linear Regression Training Project: Ecommerce Clients

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import statsmodels.api as sm
import math

# %% [markdown]
# ## Getting the Data

# Load the dataset
customers = pd.read_csv("Day20/Project2/Ecommerce_Customers")

# Display dataset info
print(customers.head())
print(customers.info())
print(customers.describe())

# %% [markdown]
# ## Exploratory Data Analysis

# Jointplot: Time on Website vs. Yearly Amount Spent
sns.jointplot(x="Time on Website", y="Yearly Amount Spent", data=customers, alpha=0.5)

# Jointplot: Time on App vs. Yearly Amount Spent
sns.jointplot(x="Time on App", y="Yearly Amount Spent", data=customers, alpha=0.5)

# Pairplot
sns.pairplot(customers, kind="scatter", plot_kws={"alpha": 0.4}, diag_kws={"bins": 40})

# Regression plot: Length of Membership vs. Yearly Amount Spent
sns.lmplot(
    x="Length of Membership",
    y="Yearly Amount Spent",
    data=customers,
    scatter_kws={"alpha": 0.3},
)

plt.show()

# %% [markdown]
# ## Splitting the Data

# Define predictors (X) and output (y)
X = customers[
    ["Avg. Session Length", "Time on App", "Time on Website", "Length of Membership"]
]
y = customers["Yearly Amount Spent"]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# %% [markdown]
# ## Training the Model with SciKit Learn

# Initialize and train the linear regression model
lm = LinearRegression()
lm.fit(X_train, y_train)

# Display coefficients
print("Coefficients:", lm.coef_)

# R-squared score
print("R-squared Score:", lm.score(X_train, y_train))

# Coefficients in a DataFrame
coef_df = pd.DataFrame(lm.coef_, X.columns, columns=["Coefficient"])
print(coef_df)

# %% [markdown]
# ## Training the Model with OLS

# Add constant to X_train for OLS
X_const = sm.add_constant(X_train)
model = sm.OLS(y_train, X_const)
model_fit = model.fit()

# Display OLS summary
print(model_fit.summary())

# %% [markdown]
# ## Predicting Test Data

# Make predictions
predictions = lm.predict(X_test)

# Scatter plot of actual vs. predicted values
sns.scatterplot(x=y_test, y=predictions)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Yearly Amount Spent vs. Model Predictions")
plt.show()

# %% [markdown]
# ## Model Evaluation

# Calculate evaluation metrics
print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("Mean Squared Error:", mean_squared_error(y_test, predictions))
print("Root Mean Squared Error:", math.sqrt(mean_squared_error(y_test, predictions)))

# %% [markdown]
# ## Residuals Analysis

# Residuals
residuals = y_test - predictions

# Plot residuals distribution
sns.histplot(residuals, bins=30, kde=True)
plt.title("Residuals Distribution")
plt.show()

# Probability plot for residuals
import pylab
import scipy.stats as stats

stats.probplot(residuals, dist="norm", plot=pylab)
pylab.show()

# %% [markdown]
# ## Conclusion

# Based on the analysis, we conclude:
# - Length of Membership is the strongest predictor of Yearly Amount Spent.
# - Time on App has a stronger influence than Time on Website.
# - Time on Website has little to no correlation with Yearly Amount Spent.
