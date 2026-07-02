# 📈 Sales Forecasting using Time Series Analysis (ARIMA)

A runnable **Data Analytics and Machine Learning** project that forecasts future sales using historical sales data through **Time Series Analysis**. This project implements the **ARIMA (AutoRegressive Integrated Moving Average)** model and provides an interactive **Streamlit dashboard** for visualizing sales trends, analyzing historical performance, and predicting future sales.


## What It Includes

- Interactive Streamlit Dashboard
- CSV Dataset Upload
- Automatic Data Cleaning & Preprocessing
- Monthly Sales Aggregation
- Historical Sales Trend Analysis
- Interactive Plotly Charts
- Moving Average Analysis (3, 6, and 12 Months)
- ARIMA Time Series Forecasting
- Configurable ARIMA Parameters (p, d, q)
- Future Sales Prediction
- Forecast Visualization
- Download Forecast Results (CSV)
- KPI Dashboard
- Dataset Statistics
- ARIMA Model Summary


## Project Structure

```text
Sales_Forecasting/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── SuperStoreOrders.csv
│
├── models/
│   └── arima_model.pkl
│
├── notebooks/
│   └── Sales_Forecasting.ipynb
│
├── outputs/
│   ├── forecast.csv
│   ├── sales_trend.png
│   └── forecast_plot.png
│
├── reports/
│   └── analytics_report.md
│
└── assets/
    ├── dashboard.png
    └── forecast.png
```

---

## Setup

Create Virtual Environment

```powershell
python -m venv sales_env
```

Activate Virtual Environment

```powershell
.\sales_env\Scripts\Activate.ps1
```

Install Required Packages

```powershell
pip install -r requirements.txt
```


## Run the Application

```powershell
streamlit run app.py
```

If you want to run Streamlit without activating the virtual environment:

```powershell
.\sales_env\Scripts\streamlit.exe run app.py
```


## Dataset

The application accepts a CSV file containing sales data with fields such as:

- Order Date
- Sales
- Product
- Category
- Customer
- Region
- Market

The uploaded dataset is automatically cleaned and transformed into a monthly time series before training the forecasting model.


## Workflow

```text
Upload Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Date Conversion
        │
        ▼
Monthly Sales Aggregation
        │
        ▼
Sales Trend Analysis
        │
        ▼
Train ARIMA Model
        │
        ▼
Generate Forecast
        │
        ▼
Display Dashboard
        │
        ▼
Download Forecast Results
```


## Dashboard Features

### 📂 Dataset Upload

Upload any supported sales dataset in CSV format.

### 📋 Dataset Preview

View uploaded records before analysis.

### 📊 KPI Dashboard

Displays:

- Total Sales
- Average Monthly Sales
- Highest Sales
- Lowest Sales

### 📈 Sales Trend Analysis

Interactive visualization of monthly sales using Plotly.

### 📉 Moving Average

Displays:

- 3-Month Moving Average
- 6-Month Moving Average
- 12-Month Moving Average

### 🤖 Forecasting

Generate future sales predictions using the ARIMA model.

### 📥 Download Results

Download forecast data as a CSV file.

### 📄 Model Summary

View the complete statistical summary of the trained ARIMA model.


## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Matplotlib
- Statsmodels (ARIMA)
- Scikit-learn


## Python Libraries

```text
streamlit
pandas
numpy
plotly
matplotlib
statsmodels
scikit-learn
```


## Future Improvements

- Auto ARIMA Model Selection
- Facebook Prophet Forecasting
- LSTM Deep Learning Forecasting
- Confidence Interval Visualization
- Seasonal Forecasting
- Model Performance Metrics (MAE, RMSE, MAPE)
- Database Integration
- User Authentication
- Business Intelligence Dashboard
- Cloud Deployment using Docker and AWS


## Learning Outcomes

This project demonstrates practical knowledge of:

- Time Series Analysis
- Data Cleaning & Preprocessing
- Data Visualization
- ARIMA Forecasting
- Streamlit Dashboard Development
- Interactive Plotly Charts
- Machine Learning Workflow
- Python Programming
- Git & GitHub


## Deployment

This application can be deployed using:

- Streamlit Community Cloud
- Render
- Hugging Face Spaces
- Docker
- Microsoft Azure
- AWS EC2


## Main Files

- `app.py` — Main Streamlit dashboard application.
- `requirements.txt` — Project dependencies.
- `README.md` — Project documentation.
- `data/SuperStoreOrders.csv` — Sales dataset.
- `models/arima_model.pkl` — Trained ARIMA model.
- `outputs/forecast.csv` — Forecast results.
- `outputs/sales_trend.png` — Historical sales visualization.
- `outputs/forecast_plot.png` — Forecast visualization.
- `notebooks/Sales_Forecasting.ipynb` — Data analysis notebook.


## Author

**Vinit Gahukar**

Bachelor of Engineering (B.E.) in Electronics and Telecommunication Engineering

Passionate about **Data Analytics, Machine Learning, Artificial Intelligence, Python Development, and Time Series Forecasting**.

- **GitHub:** https://github.com/009vinit
- **LinkedIn:** https://www.linkedin.com/in/vinit-gahukar-a9512531a
  


