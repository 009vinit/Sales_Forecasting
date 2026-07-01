import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

st.set_page_config(page_title="Sales Forecasting", layout="wide")

st.title("📈 Sales Forecasting using ARIMA")
st.write("Forecast future sales using Time Series Analysis.")

# Upload dataset
uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset")
    st.dataframe(df.head())

    # Convert order_date
    df['order_date'] = pd.to_datetime(
        df['order_date'],
        format='mixed',
        dayfirst=True,
        errors='coerce'
    )

    # Remove invalid dates
    df = df.dropna(subset=['order_date'])

    # Convert sales to numeric
    df['sales'] = (
        df['sales']
        .astype(str)
        .str.replace(',', '', regex=False)
    )

    df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

    # Remove invalid sales
    df = df.dropna(subset=['sales'])

    # Set index
    df.set_index('order_date', inplace=True)

    # Monthly Sales (Pandas 2.2+)
    sales = df['sales'].resample('ME').sum()

    st.subheader("Monthly Sales Trend")

    fig, ax = plt.subplots(figsize=(12,5))
    ax.plot(sales)
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.grid(True)

    st.pyplot(fig)

    # Train ARIMA Model
    model = ARIMA(sales, order=(5,1,0))
    model_fit = model.fit()

    # Forecast next 6 months
    forecast = model_fit.forecast(steps=6)

    st.subheader("Next 6 Months Forecast")

    st.dataframe(forecast)

    # Forecast Plot
    fig2, ax2 = plt.subplots(figsize=(12,5))

    ax2.plot(sales, label="Actual Sales", linewidth=2)
    ax2.plot(forecast.index, forecast.values,
             label="Forecast", linewidth=2)

    ax2.set_xlabel("Date")
    ax2.set_ylabel("Sales")
    ax2.legend()
    ax2.grid(True)

    st.pyplot(fig2)