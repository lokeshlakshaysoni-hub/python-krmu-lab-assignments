# Weather Data Analysis Lab

## Context
Climate awareness is crucial in today’s world. This lab assignment helps students analyze local weather data and derive meaningful insights through visualization. The report can contribute to a campus sustainability initiative.

## Learning Objectives
- Load and clean real-world CSV datasets with Pandas.
- Compute statistics using NumPy and group-by operations.
- Create informative plots using Matplotlib.
- Apply storytelling techniques to present insights.
- Automate analysis and export summaries in Python.

## Tasks
1. **Data Acquisition and Loading**
   - Download a real CSV file of local or open-source weather data (e.g., Kaggle, IMD).
   - Load into Pandas and inspect with `.head()`, `.info()`, `.describe()`.

2. **Analysis**
   - Compute daily average temperature.
   - Compute weekly rainfall totals.
   - Identify peak rainfall day.

3. **Visualization**
   - Line plot of daily average temperature.
   - Bar chart of weekly rainfall.

4. **Persistence**
   - Export cleaned dataset (`cleaned_weather_data.csv`).
   - Save summary report (`summary.txt`).
   - Save visualization (`weather_dashboard.png`).

## Outputs
- `cleaned_weather_data.csv`
- `summary.txt`
- `weather_dashboard.png`

## Requirements
- Python 3.8+
- Libraries: `pandas`, `numpy`, `matplotlib`

Install dependencies:
```bash
pip install pandas numpy matplotlib
