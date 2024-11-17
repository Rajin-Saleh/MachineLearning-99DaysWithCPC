# Data Analysis of Airbnb Listings

This project aims to analyze Airbnb listings data to gain insights into various factors affecting prices, room types, availability, and more. The dataset contains information on various properties, including their price, room type, availability, reviews, and host details.

## Project Overview

The goal of this analysis is to:

1. Clean and preprocess the data.
2. Perform Exploratory Data Analysis (EDA) to uncover insights.
3. Visualize key metrics using different types of plots.
4. Detect outliers and correlations between different variables.
5. Analyze how features like the number of bedrooms, room type, and host status influence the price.

## Dataset

The dataset used in this project is `listings.csv`, containing the following columns:

- `id`: Unique identifier for the listing.
- `name`: Name of the listing.
- `host_id`: Unique identifier for the host.
- `host_name`: Name of the host.
- `host_since`: Date when the host started.
- `host_response_time`: Time it takes for the host to respond.
- `host_response_rate`: Response rate of the host.
- `host_is_superhost`: Indicates whether the host is a superhost.
- `neighbourhood_cleansed`: Cleansed neighbourhood name.
- `neighbourhood_group_cleansed`: Cleansed group of the neighbourhood.
- `latitude`: Latitude of the listing.
- `longitude`: Longitude of the listing.
- `property_type`: Type of the property.
- `room_type`: Type of room (e.g., Entire home/apt, Private room).
- `accommodates`: Number of people the property can accommodate.
- `bathrooms`: Number of bathrooms.
- `bedrooms`: Number of bedrooms.
- `beds`: Number of beds.
- `price`: Price per night for the listing.
- `minimum_nights`: Minimum nights required to book the listing.
- `availability_365`: Number of days the listing is available in a year.
- `number_of_reviews`: Total number of reviews for the listing.
- `review_scores_rating`: Rating of the listing based on reviews.
- `license`: License details.
- `instant_bookable`: Whether the listing can be booked instantly.

## Requirements

Before running the script, make sure to install the required libraries:

```bash
pip install pandas matplotlib seaborn numpy

Script: data_analysis.py

The main script for this project is data_analysis.py. This script:

    Loads the dataset and performs data cleaning.
    Visualizes key insights such as the distribution of prices, room types, and price vs. accommodation.
    Creates a correlation heatmap to explore relationships between numerical features.
    Generates various plots, including histograms, box plots, and scatter plots.
    Analyzes outliers and compares price trends across different features like room types and host status.

Visualizations

The following visualizations are generated in the project:

    Price Distribution: A histogram showing the distribution of prices across listings.
    Room Type Distribution: A bar chart showing the distribution of room types.
    Price vs. Accommodates: A scatter plot to visualize the relationship between price and the number of people the listing accommodates.
    Price vs. Bedrooms: A scatter plot showing the relationship between the number of bedrooms and the price.
    Price Distribution by Room Type: A box plot to compare prices across different room types.
    Correlation Matrix: A heatmap showing the correlation between different numerical variables in the dataset.
    Availability vs. Price: A scatter plot to examine how availability affects price.
    Price per Bedroom: A histogram showing the distribution of price per bedroom.
    Superhost vs. Non-Superhost Price: An analysis comparing prices for superhost and non-superhost listings.
    Outlier Detection: A box plot to detect outliers in the price data.
    Price vs. Review Scores: A scatter plot to examine the relationship between review scores and price.

How to Run

    Clone the repository or download the files to your local machine.

    Make sure you have Python installed (version 3.x is recommended).

    Install the required libraries using the command mentioned in the Requirements section.

    Run the script with the following command:

    python data_analysis.py

    The script will generate several visualizations and print key analysis results to the console.

Results and Insights

After running the analysis, you will gain insights into:

    How different room types are priced in comparison to each other.
    Whether there are certain neighbourhoods or property types that have higher prices.
    The impact of host status (superhost or not) on pricing.
    How factors like number of bedrooms, bathrooms, and availability influence price.
    Any potential outliers in the data.

Conclusion

This project provides valuable insights into Airbnb listings and can help hosts better understand pricing dynamics. It also provides a foundation for further analysis, such as predicting prices using machine learning models.
Future Improvements

    Implement machine learning models for price prediction based on various features.
    Expand the dataset to include more factors, such as guest satisfaction, amenities, or seasonal trends.
    Create an interactive dashboard using tools like Dash or Streamlit for dynamic data exploration.