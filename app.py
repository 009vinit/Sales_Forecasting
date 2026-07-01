import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Sales Forecasting using ARIMA",
    page_icon="📈",
    layout="wide"
)

# ---------------------------
# HEADER
# ---------------------------
st.title("📈 Sales Forecasting using ARIMA")
st.markdown("Forecast future sales using **Time Series Analysis**.")

st.markdown("---")

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.header("⚙️ Model Settings")

forecast_months = st.sidebar.slider(
    "Forecast Months",
    min_value=1,
    max_value=24,
    value=6
)

p = st.sidebar.slider("AR (p)", 0, 5, 5)
d = st.sidebar.slider("Difference (d)", 0, 2, 1)
q = st.sidebar.slider("MA (q)", 0, 5, 0)

st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Project**

    Sales Forecasting using ARIMA

    Built with:
    - Streamlit
    - Plotly
    - Pandas
    - Statsmodels
    """
)

# ---------------------------
# FILE UPLOAD
# ---------------------------
uploaded_file = st.file_uploader(
    "📂 Upload Sales CSV",
    type=["csv"]
)

if uploaded_file is not None:

    # ---------------------------
    # READ DATA
    # ---------------------------
    df = pd.read_csv(uploaded_file)

    # Convert Date
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        format="mixed",
        dayfirst=True
    )

    # Convert Sales
    df["sales"] = (
        df["sales"]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

    df.set_index("order_date", inplace=True)

    # Monthly Sales
    sales = df["sales"].resample("ME").sum()

    # ---------------------------
    # DATASET
    # ---------------------------
    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    # ---------------------------
    # SALES SUMMARY
    # ---------------------------
    st.subheader("📊 Sales Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Sales",
        f"${sales.sum():,.0f}"
    )

    col2.metric(
        "Average Monthly",
        f"${sales.mean():,.0f}"
    )

    col3.metric(
        "Highest",
        f"${sales.max():,.0f}"
    )

    col4.metric(
        "Lowest",
        f"${sales.min():,.0f}"
    )

    st.markdown("---")

    # ---------------------------
    # MONTHLY SALES TREND
    # ---------------------------
    st.subheader("📈 Monthly Sales Trend")

    fig = px.line(
        x=sales.index,
        y=sales.values,
        labels={
            "x": "Date",
            "y": "Sales"
        },
        title="Monthly Sales Trend"
    )

    fig.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ---------------------------
    # TRAIN MODEL
    # ---------------------------
    with st.spinner("Training ARIMA Model..."):

        model = ARIMA(
            sales,
            order=(p, d, q)
        )

        model_fit = model.fit()

    st.success("✅ Model Trained Successfully!")

    # ---------------------------
    # FORECAST
    # ---------------------------
    forecast = model_fit.forecast(
        steps=forecast_months
    )

    # ---------------------------
    # FORECAST TABLE
    # ---------------------------
    st.subheader("📅 Forecast Table")

    forecast_df = pd.DataFrame({
        "Date": forecast.index,
        "Forecast Sales": forecast.values
    })

    st.dataframe(
        forecast_df,
        use_container_width=True
    )

    # Download Button
    csv = forecast_df.to_csv(index=False)

    st.download_button(
        label="⬇ Download Forecast CSV",
        data=csv,
        file_name="future_forecast.csv",
        mime="text/csv"
    )

    st.markdown("---")

    # ---------------------------
    # FORECAST GRAPH
    # ---------------------------
    st.subheader("📉 Actual vs Forecast")

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=sales.index,
            y=sales.values,
            mode="lines",
            name="Actual Sales"
        )
    )

    fig2.add_trace(
        go.Scatter(
            x=forecast.index,
            y=forecast.values,
            mode="lines+markers",
            name="Forecast"
        )
    )

    fig2.update_layout(
        title="Sales Forecast",
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    # ---------------------------
    # MODEL SUMMARY
    # ---------------------------
    with st.expander("📑 View ARIMA Model Summary"):

        st.text(model_fit.summary())

    # ---------------------------
    # FOOTER
    # ---------------------------
    st.markdown("---")

    st.markdown(
        """
        ### 👨‍💻 Developed By

        **Vinit Gahukar**

        Sales Forecasting using ARIMA

        Python • Streamlit • Plotly • Statsmodels
        """
    )

else:
    st.info("📂 Please upload a CSV file to begin forecasting.")