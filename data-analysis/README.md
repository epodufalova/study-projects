# Financial Analysis Project

## Overview
This project analyzes a financial dataset containing sales, profit, and product performance metrics across different countries and segments.

## Dataset
**File:** `Financial Sample.csv`
- Downloaded from Microsoft's website. Contains 700 records with 16 columns
- Includes sales data, product information, country data, and financial metrics

## Key Analysis Areas
1. **Data Exploration**: Initial data inspection and cleaning
2. **Country Performance**: Sales distribution across different countries
3. **Product Analysis**: Most popular products and their performance
4. **Profit Analysis**: Profit distribution by country
5. **Temporal Trends**: Monthly sales patterns (if temporal data available)

## Notebook Features
- **Data Cleaning**: Handling missing values and data type conversions
- **Visualizations**: 
  - Bar charts showing sales by country
  - Product popularity analysis
  - Profit distribution across countries
- **Statistical Analysis**: Descriptive statistics and correlation analysis

## Key Findings
- France shows the highest sales volume among all countries
- Specific products demonstrate significantly higher profitability

## Weather Data Analysis

## Dataset
**File:** `weather.csv`

## Overview
This Jupyter Notebook demonstrates a complete data analysis workflow using weather data. 
The project focuses on data cleaning, transformation, and visualization using Pandas and Matplotlib to analyze weather patterns and trends.

## Data Processing Steps

### 1. Data Loading and Initial Setup
The notebook begins by importing necessary libraries and checking their versions to ensure compatibility.

### 2. Data Cleaning and Transformation
The notebook performs comprehensive data cleaning:
- Stripped percentage signs from cloud cover data and converted to float
- Cleaned precipitation data by removing units and handling missing values
- Removed temperature units (°C) and converted to numeric values
- Stripped wind speed units (m/s) and converted to float
- Extracted month information from date periods

### 3. Data Filtering
Data is filtered for a specific month (November) using a calculated value for analysis.

### 4. Data Visualization
The notebook includes visualizations such as:
- Wind speed trends over time
- Temperature patterns (daily vs nightly)
- Cloud cover analysis
- Precipitation data visualization

## 📈 Key Features

- **Data Quality Handling**: Comprehensive cleaning of messy data including unit removal and missing value handling
- **Time Series Analysis**: Monthly filtering and temporal pattern recognition
- **Multiple Visualizations**: Various plots to understand weather patterns
- **Ukrainian Data Support**: Handles Ukrainian language column names appropriately

## Dependencies
- pandas
- numpy
- matplotlib
- seaborn
- jupyter



## Results
The analysis reveals patterns in sales distribution, identifies top-performing products, and highlights geographical variations in profitability.
