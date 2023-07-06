import csv
import random
from datetime import datetime, timedelta

# Define the start and end dates for the year
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Define the output CSV file name
output_file = 'temperature_data.csv'

# Define the headers for the CSV file
headers = ['Date', 'Temperature']

# Generate random temperature data for each day of the year
data = []
current_date = start_date
while current_date <= end_date:
    temperature = random.uniform(-10, 40)  # Generate random temperature between -10 and 40
    data.append([current_date.strftime('%Y-%m-%d'), temperature])
    current_date += timedelta(days=1)

# Write the data to the CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(data)

print(f"CSV file '{output_file}' generated successfully.")
