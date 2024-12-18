import json
import csv

# Path to the input JSON file
json_file_path = 'demo_deps.json'  # Update with your file path

# Path to the output CSV file
csv_file_path = 'deps.csv'  # Update with your desired file path

# Open the JSON file and read its content
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Open the CSV file and write the data
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header (keys from the first JSON object)
    header = json_data[0].keys()
    writer.writerow(header)
    
    # Write the rows (values from each JSON object)
    for item in json_data:
        writer.writerow(item.values())

print(f"CSV file has been generated at: {csv_file_path}")
