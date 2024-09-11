import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap

# Load the CSV file
airports = pd.read_csv('output.csv')

# Create a heatmap
heatmap_data = airports.groupby(['Lat', 'Long']).size().reset_index(name='count')
heatmap_points = [[row['Lat'], row['Long'], row['count']] for index, row in heatmap_data.iterrows()]
heatmap = folium.Map(location=[50, 50], zoom_start=3)


# Display the heatmap using Streamlit
st.title("FlightAttendantRosterAnalysis")
st.write("by SnuggerG")

# Create a slider for the radius
radius = st.slider("Heatmap Radius", min_value=5, max_value=30, value=15) 
# Update the heatmap based on the slider value
HeatMap(heatmap_points, radius=radius).add_to(heatmap)

st.write("Heatmap of airport visits")
st_folium(heatmap, height=500 , width=1200)





