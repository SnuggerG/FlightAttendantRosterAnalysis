import PyPDF2
import pandas as pd
import re

# Function to extract text from PDF
def extract_pdf_text(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    all_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        all_text += page.extract_text()
    return all_text

# Extract flight information
def extract_flight_info(text):
    pattern = r'(HV\d+)\s+(\d{2}:\d{2})\s+([A-Z]{3})\s+(\d{2}:\d{2})\s+([A-Z]{3})\s+(\d{2}:\d{2})\s+([A-Z0-9]+)'
    matches = re.findall(pattern, text)
    return pd.DataFrame(matches, columns=['Flight Number', 'Signin Time', 'Departure Airport', 'Departure Time', 'Arrival Airport', 'Arrival Time', 'Aircraft Type'])

# Main flow
pdf_file = 'Roster.pdf'
output_csv = 'flight_roster.csv'

pdf_text = extract_pdf_text(pdf_file)
print("PDF Text:")
print(pdf_text)
print("======================================")
flight_info = extract_flight_info(pdf_text)
print("\nFlight Information:")
print(flight_info)
print("======================================")
# Save to CSV
flight_info.to_csv(output_csv, index=False)
print(f"Data saved to {output_csv}")
print("======================================")
# Display the entire CSV file
print("\nCSV File:")
flight_info_csv = pd.read_csv(output_csv)
print(flight_info_csv)
print("======================================")