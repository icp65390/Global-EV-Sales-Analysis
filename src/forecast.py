import pandas as pd
import numpy as np

df = pd.read_csv("data/ev_sales_2015_2025.csv")

growth_rate = np.mean(df["EV_Sales_Million"].pct_change().dropna())

future_years = list(range(2026, 2036))
last_value = df["EV_Sales_Million"].iloc[-1]

forecast = []
for year in future_years:
    last_value = last_value * (1 + growth_rate)
    forecast.append([year, round(last_value, 2)])

forecast_df = pd.DataFrame(forecast, columns=["Year", "Forecast_EV_Sales_Million"])
print(forecast_df)

