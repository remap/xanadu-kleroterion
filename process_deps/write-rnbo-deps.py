import csv
import json

csv_file_path = 'deps.csv'  # Update with your file path
json_file_path = 'xanadu-rnbo-dependencies.json'  # Update with your desired file path

with open(csv_file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)    
    json_data = [row for row in reader]

search_term = "https://static.8thwall.app/"
replace_term = "/xanadu/"

# Write the JSON data to a file with pretty-printing
with open(json_file_path, 'w') as json_file:
    json_file.write(json.dumps(json_data, indent=4).replace(search_term,replace_term))

print(f"JSON file has been generated at: {json_file_path}")
