import airportsdata
import pandas as pd
import csv

# Load the airport data
airports = airportsdata.load('IATA')

# Reading the csv file
df = pd.read_csv('flights.csv')

# Initialize a counter to keep track of the number of conversions
conversion_count = 0

# Create a list to store the output data
output_data = []

# Iterate over each row in the CSV file
for index, row in df.iterrows():
    # Get the IATA code from the "Departure Airport" column and convert to uppercase
    iata_code = row['Departure Airport'].upper()

    # Check if the airport exists in the dictionary
    if iata_code in airports:
        airport = airports[iata_code]
        longitude = airport['lon']
        latitude = airport['lat']
        print(f'The longitude and latitude of {iata_code} are {longitude} and {latitude}')
        conversion_count += 1
        # Append the data to the output list
        output_data.append([iata_code, longitude, latitude])
    else:
        print(f'{iata_code} -> NOT FOUND')

# Print the total number of conversions
print(f'Total conversions: {conversion_count}')

# Write the output data to a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IATA", "Long", "Lat"])  # header row
    writer.writerows(output_data)
