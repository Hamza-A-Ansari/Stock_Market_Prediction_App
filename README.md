# Time Series Stock Market Price Prediction Web App in Python

## Overview

This Python application is designed to forecast stock market prices for a selected company using time series analysis. It utilizes the yfinance library to fetch historical stock market data within a user-defined time frame. The forecasting is performed using the SARIMAX machine learning model, and Plotly is employed for data visualizations.

## Features

- **Data Fetching**: The app allows users to input start and end dates to fetch historical stock market data for a selected company from Yahoo Finance.

- **Data Visualization**: The application provides interactive visualizations of the stock market data, enabling users to explore the closing prices over time.

- **Data Decomposition**: It decomposes the time series data into trend, seasonality, and residuals using the seasonal_decompose function from statsmodels.

- **Model Training**: Users can select parameters such as p, d, q, and seasonal_order for the SARIMAX model to be fitted on the historical data.

- **Model Evaluation**: The stationarity of the data is checked using the Augmented Dickey-Fuller (ADF) test. The summary of the SARIMAX model is also displayed.

- **Prediction**: Users can input the number of days for future price prediction, and the app displays both the predicted and actual values.

- **Interactive Plots**: The app provides interactive Plotly charts to compare actual and predicted stock prices over time.

## Usage

1. **Select Company and Date Range**: Choose a company from the provided list and set the start and end dates for fetching historical stock market data.

2. **Data Visualization**: Explore the visual representation of the historical stock prices and select a specific column for prediction.

3. **Model Configuration**: Set the parameters (p, d, q, and seasonal_order) for the SARIMAX model.

4. **Model Training**: Fit the SARIMAX model on the historical data, view the model summary, and check the stationarity of the data.

5. **Prediction**: Input the number of days for future price prediction, and the app displays both the predicted and actual values.

6. **Interactive Plots**: Compare actual and predicted stock prices using the interactive Plotly chart.

## Dependencies

- streamlit
- yfinance
- pandas
- plotly
- statsmodels

## Installation

```bash
pip install streamlit yfinance pandas plotly statsmodels
```

## How to Run

```bash
streamlit run app.py
```
Replace 'app.py' with the name of your Python script containing the code.

## Acknowledgements

- **Streamlit**
- **yfinance**
- **Plotly**
- **statsmodels**

## Interface Screenshots

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/d9ef6a7f-d8e1-431b-bc47-a4c5e9b1852f)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/de7c3775-708c-4155-8e12-6d1504be991c)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/74b95de5-b76b-4b05-bfb3-bea591a52634)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/99469909-2e72-427b-b1c6-9272f0ea6ac1)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/3560a88c-ff2a-4618-900a-ef47d4776ca1)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/5119b0ae-b331-4f5b-b282-b9fef0002c26)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/229c9cab-a03d-43fe-b366-1d34315330d7)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/db5e6cf0-3aa7-416f-84de-2bc80768d67b)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/6934c432-2596-457a-be1b-b434a7de7c6a)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/9db0b749-9545-4832-b9a0-66ffe613a820)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/f261bf02-a3a0-4052-bad7-f5d882a9d0d6)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/25e27ef2-fe8e-49a5-9290-9d3cbecbc522)

![image](https://github.com/Hamza-A-Ansari/Stock_Market_Prediction_App/assets/93026830/a6c44a2e-c5cb-4ece-87bb-19a1ed845138)

<p align="center" style="font-size: 18px; color: #333;">
 <strong> Feel free to contribute, report issues, or suggest improvements. Happy Coding! </strong>
</p>
