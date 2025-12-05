import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv("weather_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

print(df.head())
print(df.info())
print(df.describe())

daily_temp = df.groupby(df["Date"].dt.date)["Temperature_C"].mean()
weekly_rain = df.resample("W", on="Date")["Rainfall_mm"].sum()

fig, ax = plt.subplots(2, 1, figsize=(8, 8))
ax[0].plot(daily_temp.index, daily_temp.values)
ax[0].set_title("Daily Average Temperature (°C)")
ax[1].bar(weekly_rain.index, weekly_rain.values)
ax[1].set_title("Weekly Rainfall (mm)")
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.close()

df.to_csv("cleaned_weather_data.csv", index=False)

summary_text = f"""
Weather Data Summary Report
===========================

Total Days Recorded: {len(df)}
Average Temperature: {df['Temperature_C'].mean():.2f} °C
Highest Temperature: {df['Temperature_C'].max():.2f} °C
Lowest Temperature: {df['Temperature_C'].min():.2f} °C
Total Rainfall: {df['Rainfall_mm'].sum():.2f} mm
Peak Rainfall Day: {df.loc[df['Rainfall_mm'].idxmax(), 'Date'].date()}
"""

with open("summary.txt", "w") as f:
    f.write(summary_text)

print(summary_text)
