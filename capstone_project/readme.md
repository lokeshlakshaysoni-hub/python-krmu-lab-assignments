# Campus Energy-Use Dashboard

## Project Overview
This project analyzes energy consumption data across campus buildings.  
It loads multiple CSV files, aggregates consumption statistics, visualizes trends, and exports cleaned data along with a concise executive summary.

## Features
- **Data Loading**: Reads all building-level CSV files from the `data/` folder.
- **Aggregation**:
  - Daily and weekly campus consumption
  - Per-building statistics (mean, min, max, sum)
- **Object-Oriented Design**:
  - `Building` class for individual building data
  - `BuildingManager` class to manage multiple buildings
- **Visualization**:
  - Line chart of daily consumption
  - Bar chart of building totals
  - Scatter plot of weekly consumption
- **Persistence**:
  - Saves cleaned dataset (`cleaned_energy_data.csv`)
  - Saves building summary (`building_summary.csv`)
  - Generates executive summary (`summary.txt`)
- **Dashboard Image**:
  - Combined visualization saved as `dashboard.png`

## Folder Structure

Name - Lokesh Verma 
roll no. - 2501730182
