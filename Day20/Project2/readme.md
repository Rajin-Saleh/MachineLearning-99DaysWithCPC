# 📊 Linear Regression Training Project: Ecommerce Clients

This project analyzes customer data from an e-commerce website to help the company make data-driven decisions about improving their app and website experiences. Using Python and machine learning, we build a linear regression model to determine which factors most influence customer spending.

---

## 🔍 Project Overview

### Dataset

The dataset contains information about customers, including:

- **Avg. Session Length**: Average session time of in-store style advice sessions.
- **Time on App**: Average time spent on the mobile app in minutes.
- **Time on Website**: Average time spent on the website in minutes.
- **Length of Membership**: Duration of the customer’s membership in years.

### Objective

To identify the factors that most impact yearly customer spending and determine whether the company should focus more on improving their **app experience** or **website experience**.

---

## 🚀 Features

- **Exploratory Data Analysis (EDA)**:
  - Visualizations with `Seaborn` to identify patterns and correlations.
- **Machine Learning**:
  - Multivariable Linear Regression using `Scikit-Learn`.
  - Model evaluation with metrics like Mean Absolute Error (MAE) and R-squared.
- **Advanced Analysis**:
  - Ordinary Least Squares (OLS) regression using `Statsmodels` for detailed insights.
- **Residual Analysis**:
  - Residual distribution and normality checks.

---

## 📁 Project Structure

project/ │ ├── Day20/Project2/Ecommerce_Customers.csv # Dataset ├── ecommerce_linear_regression.py # Main Python script └── README.md # Project documentation

---

## 🛠️ Tools and Libraries

- **Python** for scripting
- **Pandas** for data manipulation
- **Matplotlib** and **Seaborn** for data visualization
- **Scikit-learn** for machine learning
- **Statsmodels** for advanced statistical analysis
- **SciPy** for residual analysis

---

## 📊 Key Insights

1. **Length of Membership** is the most significant predictor of yearly spending.
2. **Time on App** has a moderate impact on spending, indicating the app’s potential for growth.
3. **Time on Website** has little correlation with spending, suggesting the need for improvement in the desktop experience.

---

## 📈 Model Performance

### Metrics

- **Mean Absolute Error (MAE)**: Low values indicate accurate predictions.
- **R-squared Score**: High score (~1) shows a good fit to the data.

### Evaluation Results

- Detailed evaluation metrics are included in the script output.

---

📜 Conclusion

This project demonstrates the power of linear regression in understanding customer behavior. By focusing on mobile app improvements and length of membership programs, the company can maximize customer spending