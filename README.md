# Financial Log Return & Variance Analysis

## Overview
This project analyzes gold and crude oil price data by calculating log returns and variance (a proxy for volatility).

It also demonstrates how to import financial and macroeconomic data using:

- FRED API (NASDAQ 100 Index)
- World Bank API (GDP and Export data)

## Technologies Used
- Python
- pandas
- numpy
- pandas-datareader

## What This Project Does
- Loads historical gold and crude oil prices from CSV files
- Converts price columns to numeric format
- Calculates log returns
- Computes variance of returns
- Imports macroeconomic datasets for comparison

## Log Return Formula
Log return is calculated as:

log(current_price / previous_price)

This is commonly used in finance for time series analysis.

## How to Run

Install dependencies:

pip install pandas numpy pandas-datareader

Run the script:

python financial_log_return_analysis.py

## Required Files

The project requires two CSV files in the same directory:

- gold_prices.csv (must contain column: Gold_Price)
- crude_oil_prices.csv (must contain column: Crude_Oil_Price)

## Output
The script prints:
- Gold return variance
- Crude oil return variance
