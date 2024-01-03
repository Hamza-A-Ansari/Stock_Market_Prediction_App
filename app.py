# Import Libraries
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import date
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

# Title
title = 'Stock Market Prediction App'
st.title(title)

# Sub Header
st.subheader('This App is created to forecast the stock market price of the selected company')

# Add an image from online resource
st.image("https://www.analytixlabs.co.in/blog/wp-content/uploads/2021/09/Blog-4-Title-Banner.jpg")

# Adding Side bar
st.sidebar.header("Select the parameters from below")

# Take input of start and end date from user
start_date = st.sidebar.date_input('Start Date', date(2020, 1, 1))
end_date = st.sidebar.date_input('End Date', date(2020, 12, 31))

# Add ticker symbol list
ticker_list = ["AAPL", "MSFT", "GOOG", "GOOGL", "META", "TSLA", "NVDA", "ADBE", "PYPL", "INTC", "CMCSA", "NFLX", "PEP"]
ticker = st.sidebar.selectbox('Select the Company', ticker_list)

# Fetch data from user input using yfinance labrary
data = yf.download(ticker, start=start_date, end=end_date)

# Adding index column
data.insert(0, "Date", data.index, True)
data.reset_index(drop = True, inplace = True)

# Print the data
st.write('### Data from', start_date, 'to', end_date)
st.write(data)

# Plot the Data
st.header('Data Visualization')
st.subheader('Plot of the Data')
st.write('**Note:** Select specific date range on the sidebar, or zoom in on the plot and select your specific column')
fig = px.line(data, x='Date', y=data.columns, title='Closing price of the Stock')
st.plotly_chart(fig)

# Add a select box to select column from data
column = st.selectbox('Select the column to be used for prediction', data.columns[1:])

# Subsetting the Data
data = data[['Date', column]]
st.write('Selected Data')
st.write(data)

# ADF test check stationarity
st.header('Is Data stationary')
st.write(adfuller(data[column])[1] < 0.05)

# Lets decompose the Data
st.header('Decomposition of the Data')
decomposition = seasonal_decompose(data[column], model='additive', period=12)
st.write(decomposition.plot())

# Make same plot in Plotly
st.write("## Plotting the decomposition in Plotly")
st.plotly_chart(px.line(x=data['Date'], y=decomposition.trend, title="Trend", width=1200, height=400, labels={'x': 'Date', 'y': 'Price'}).update_traces(line_color='Blue'))
st.plotly_chart(px.line(x=data['Date'], y=decomposition.seasonal, title="Seasonality", width=1200, height=400, labels={'x': 'Date', 'y': 'Price'}).update_traces(line_color='green'))
st.plotly_chart(px.line(x=data['Date'], y=decomposition.resid, title="Residuals", width=1200, height=400, labels={'x': 'Date', 'y': 'Price'}).update_traces(line_color='Red', line_dash='dot'))

# User input for three parameters of the model and seasonal order
p = st.slider('Select the value of p', 0, 5, 2)
d = st.slider('Select the value of d', 0, 5, 1)
q = st.slider('Select the value of q', 0, 5, 2)
seasonal_order = st.number_input('Select the value of seasonal p', 0, 24, 12)

# Fitting our machine learning model
model = sm.tsa.statespace.SARIMAX(data[column], order=(p, d, q), seasonal_order=(p, d, q, seasonal_order))
model = model.fit()

# Print the model summary
st.header('Model Summary')
st.write(model.summary())
st.write("-----")

# Header for Prediction part
st.write("<p style='color:green; font-size: 50px; font-weight: bold;'>Predicting the Data</p>")

# User input of how many prediction days
forecast_period = st.number_input('Slect the number of days of Prediction', 1, 365, 10)

# Predict the values
predictions = model.get_prediction(start=len(data), end=len(data) + forecast_period)
predictions = predictions.predicted_mean

# Add index to the predictions
predictions.index = pd.date_range(start=end_date, periods=len(predictions), freq = 'D')
predictions = pd.DataFrame(predictions)
predictions.insert(0, "Date", predictions.index, True)
predictions.reset_index(drop=True, inplace=True)

# Print actual and predicted values
st.write("Predicted Values", predictions)
st.write("Actual Values", data)
st.write("-----")

# Plot the Data
fig = go.Figure()

# Add Actual data to the plot
fig.add_trace(go.Scatter(x = data['Date'], y = data[column], mode='lines', name='Actual', line = dict(color='blue')))

# Add Predicted data to the plot
fig.add_trace(go.Scatter(x = predictions['Date'], y = predictions["predicted_mean"], mode='lines', name='Predicted', line = dict(color='red')))

# Set the Title and axis Labels
fig.update_layout(title='Actual vs Predicted', xaxis_title = 'Date', yaxis_title = 'Price', width=1000, height=400)

# Display the plot
st.plotly_chart(fig)

# Add "Show" button to show plots
show_plots = False
if st.button('Show Separate Plots'):
    if not show_plots:
        st.write(px.line(x=data['Date'], y=data[column], title="Actual", width=1200, height=400, labels={'x': 'Date', 'y': 'Price'}).update_traces(line_color='Blue'))
        st.write(px.line(x=predictions['Date'], y=predictions["predicted_mean"], title="Predicted", width=1200, height=400, labels={'x': 'Date', 'y': 'Price'}).update_traces(line_color='green'))
        show_plots = True
    else:
        show_plots = False

# Add "Hide" button to hide plots
hide_plots = False
if st.button('Hide Separate Plots'):
    if not hide_plots:
        hide_plots = True
    else:
        hide_plots = False
st.write("-----")