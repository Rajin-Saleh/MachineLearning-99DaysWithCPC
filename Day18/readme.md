# IKEA Products Data Analysis

This project involves analyzing an IKEA dataset to extract insights and visualize various aspects of the data, such as product prices, categories, dimensions, and more.

## Dataset Overview

The dataset (`ikea2.csv`) contains information about IKEA products, including:

- **Columns**:
  - `item_id`: Unique identifier for each product.
  - `name`: Product name.
  - `category`: Product category.
  - `price`: Current price of the product.
  - `old_price`: Previous price of the product (if available).
  - `sellable_online`: Indicates whether the product is available online.
  - `link`: URL to the product page.
  - `other_colors`: Availability of other color options.
  - `short_description`: Brief description of the product.
  - `designer`: Name of the product designer.
  - `depth`, `height`, `width`: Dimensions of the product.
  - `product_description`: Detailed description of the product.
  - `current_status`: Current availability status.
  - `keywords`: Associated keywords.
  - `topic_group`: Product grouping.
  - `topic_desc`: Additional topic information.

## Analysis Performed

1. **General Overview**:
   - Total number of products, categories, designers, and availability statuses.

2. **Price Analysis**:
   - Distribution of product prices.
   - Analysis of products with old prices and price differences.

3. **Category Insights**:
   - Number of products per category.
   - Average price per category.

4. **Online Sales Analysis**:
   - Proportion of products available for online purchase.
   - Average price comparison for online vs offline products.

5. **Dimensional Analysis**:
   - Heatmap of average product dimensions by category.

6. **Designer Popularity**:
   - Top designers by the number of products.
   - Average price of products by designer.

7. **Word Clouds**:
   - Visualization of common words in product descriptions.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `pandas` for data manipulation
  - `matplotlib` and `seaborn` for visualization
  - `wordcloud` for generating word clouds

## How to Run

1. Place the dataset (`ikea2.csv`) in the same directory as the script.
2. Run the Python script to generate the analysis and visualizations.
3. View the outputs interactively; graphs and visualizations are displayed directly.
