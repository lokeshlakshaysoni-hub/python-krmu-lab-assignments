import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

files = [f for f in os.listdir("data") if f.endswith(".csv")]
df_list = []
for f in files:
    try:
        temp = pd.read_csv(os.path.join("data", f))
        temp["building"] = f.replace(".csv", "")
        df_list.append(temp)
    except:
        print("Error loading:", f)

df = pd.concat(df_list, ignore_index=True)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.set_index("timestamp")

daily = df.resample("D")["kwh"].sum()
weekly = df.resample("W")["kwh"].sum()
building_sum = df.groupby("building")["kwh"].agg(["mean", "min", "max", "sum"])

class Building:
    def __init__(self, name):
        self.name = name
        self.data = df[df["building"] == name]
    def total(self):
        return self.data["kwh"].sum()

class BuildingManager:
    def __init__(self, names):
        self.buildings = [Building(n) for n in names]

manager = BuildingManager(df["building"].unique())

fig, ax = plt.subplots(3, 1, figsize=(8, 10))
ax[0].plot(daily.index, daily.values)
ax[0].set_title("Daily Consumption")
ax[1].bar(building_sum.index, building_sum["sum"])
ax[1].set_title("Building Total Consumption")
ax[2].scatter(weekly.index, weekly.values)
ax[2].set_title("Weekly Consumption")
plt.tight_layout()
plt.savefig("dashboard.png")
plt.close()

df.to_csv("cleaned_energy_data.csv")
building_sum.to_csv("building_summary.csv")

total_consumption = df["kwh"].sum()
highest_building = building_sum["sum"].idxmax()
peak_load_day = daily.idxmax()
df["DayOfWeek"] = df.index.day_name()
weekly_trends = df.groupby("DayOfWeek")["kwh"].mean()

with open("summary.txt", "w") as f:
    f.write("Campus Energy Summary\n")
    f.write("=====================\n\n")
    f.write(f"Total Campus Consumption: {total_consumption}\n")
    f.write(f"Highest-Consuming Building: {highest_building}\n")
    f.write(f"Peak Load Day: {peak_load_day}\n\n")
    f.write("Weekly/Daily Trends:\n")
    f.write(weekly_trends.to_string())

print("Done!")
