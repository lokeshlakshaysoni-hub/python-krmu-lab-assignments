# Name:Lokesh Verma
# Project Title: Campus Energy-Use Dashboard

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# -----------------------------
# TASK 1: LOAD ALL CSV FILES
# -----------------------------
files = [f for f in os.listdir("data") if f.endswith(".csv")]
df_list = []

for f in files:
    try:
        temp = pd.read_csv("data/" + f)
        temp["building"] = f.replace(".csv", "")
        df_list.append(temp)
    except:
        print("Error loading:", f)

df = pd.concat(df_list, ignore_index=True)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# -----------------------------
# TASK 2: SIMPLE AGGREGATION
# -----------------------------
df = df.set_index("timestamp")

daily = df.resample('D')['kwh'].sum()
weekly = df.resample('W')['kwh'].sum()
building_sum = df.groupby("building")['kwh'].agg(['mean','min','max','sum'])

# -----------------------------
# TASK 3: VERY SIMPLE OOP
# -----------------------------
class Building:
    def __init__(self, name):
        self.name = name
        self.data = df[df['building'] == name]

    def total(self):
        return self.data['kwh'].sum()

class BuildingManager:
    def __init__(self, names):
        self.buildings = [Building(n) for n in names]

manager = BuildingManager(df['building'].unique())

# -----------------------------
# TASK 4: VISUALIZATION
# -----------------------------
fig, ax = plt.subplots(3, 1, figsize=(8, 10))

# Line – Daily
ax[0].plot(daily.index, daily.values)
ax[0].set_title("Daily Consumption")

# Bar – Building total
ax[1].bar(building_sum.index, building_sum['sum'])
ax[1].set_title("Building Total Consumption")

# Scatter – Weekly trend
ax[2].scatter(weekly.index, weekly.values)
ax[2].set_title("Weekly Consumption")

plt.tight_layout()
plt.savefig("dashboard.png")
plt.close()

# -----------------------------
# TASK 5: EXPORT + SUMMARY
# -----------------------------
df.to_csv("cleaned_energy_data.csv")
building_sum.to_csv("building_summary.csv")

with open("summary.txt", "w") as f:
    f.write("Campus Energy Summary\n")
    f.write("---------------------\n")
    f.write(f"Total Campus Consumption: {df['kwh'].sum()}\n")
    f.write(f"Highest Building: {building_sum['sum'].idxmax()}\n")
    f.write(f"Peak Load Day: {daily.idxmax()}\n")

print("Done!")
