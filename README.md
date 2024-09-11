# FlightAttendantRosterAnalysis

This project analyzes and visualizes my flight schedule as a flight attendant. The key output is an **interactive heatmap** of the most visited airports. The project follows the **data analytics cycle** and is deployed as a **Streamlit** web application.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Repository Contents](#repository-contents)
3. [Data Analytics Cycle](#data-analytics-cycle)
4. [Tools Used](#tools-used)
5. [How to Run Locally](#how-to-run-locally)
6. [Key Insights](#key-insights)
7. [Live Demo](#live-demo)
8. [Future Updates](#future-updates)

---

## Project Overview
The goal of this project is to convert my flight roster from PDF to CSV format, extract relevant data, and analyze the most visited airports, visualized on a **heatmap**. This allows me to explore and gain insights into my travel patterns.

---

## Repository Contents

The repository contains the following components:

1. **Streamlit Application**:
   - The `app.py` file is the main application script that runs the interactive Streamlit app. This app displays the heatmap of the most visited airports and other key insights. The heatmap includes a **slider** to adjust the intensity, making it easier to visualize the data.

2. **CSV File**:
   - `airports_data.csv`: Contains IATA codes and their corresponding geographical coordinates (latitude and longitude). This file is used for visualizing airport locations on the heatmap.

3. **Conversion Scripts**:
   - `pdf_to_csv_converter.py`: A Python script that converts flight roster data from PDF format to CSV. This script extracts and structures the data for further analysis.
   - `iata_to_coordinates.py`: A Python script that takes IATA airport codes from the CSV file and retrieves their geographical coordinates using the **`airportsdata`** library.

---

## Data Analytics Cycle

### 1. Ask
**Objective**: To analyze my flight schedule and answer the question—what are the most visited airports based on my flight schedule?

### 2. Prepare
**Data Source**:  
Flight roster in **PDF** format converted to **CSV**. The CSV file includes:
- **IATA codes** for airport destinations.
- **Geographical coordinates** of airports.

### 3. Process
- **PDF to CSV Conversion**: Using `pdf_to_csv_converter.py`, the flight roster was converted from PDF to CSV format.
- **Data Cleaning**: The CSV data was cleaned and formatted using **Pandas**.
- **Geocoding**: `iata_to_coordinates.py` was used to convert IATA codes to latitude and longitude coordinates with the help of the **`airportsdata`** library.

### 4. Analyze
- **Counting Visits**: Analyzed the CSV data to count how many times each airport appeared in the flight schedule.
- **Generating Heatmap**: Created a heatmap of the most visited airports using **`folium`**, including a **slider** for adjusting the intensity of the heatmap to better visualize the data.

### 5. Share
The main output is an **interactive heatmap** of the most visited airports. You can zoom, pan, and hover over the points to explore the data interactively. The heatmap includes a **slider** to adjust the intensity for better visualization.

### 6. Act
Insights from the heatmap help in understanding travel patterns and frequent routes, which could be used for optimizing future schedules.

---

## Tools Used
- **Python**, **Pandas**, **airportsdata**, **Folium**, **Streamlit**, and **PyPDF2**.

---

## How to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SnuggerG/flight-roster-analysis.git
   cd flight-roster-analysis
2. **Install Dependencies**: 
    ```bash
    pip install -r requirements.txt

3. **Run the Streamlit App**:
   ```bash
   streamlit run app.py


**Use the Conversion Scripts (if needed)**:
- To convert PDF to CSV:
  ```bash
  python pdf_to_csv_converter.py

- To get coordinates for IATA codes:
  ```bash
  python iata_to_coordinates.py

---

## Key Insights

- The interactive heatmap displays the most visited airports.
- The heatmap features a slider to adjust the intensity, helping to visualize the data more effectively.
- Frequent hubs are highlighted with more intense heat spots.

---

## Live Demo

You can explore the project and visualize the **most visited airports** on an interactive map via the **Streamlit application**.

**Check out the live version here**: [Streamlit App Link](https://flightattendantrosteranalysis-jdeg9e8gxqgefjey8c7rvr.streamlit.app)

---

## Future Updates

This repository will be updated regularly as I continue to improve the project. Planned updates include:

- Enhancing the heatmap to include temporal analysis (e.g., by month or year) for better insights.
- Expanding the analysis to include sign-in and sign-off times.
- Improving the UI of the application to make it more user-friendly and visually appealing.

Stay tuned for future improvements!
